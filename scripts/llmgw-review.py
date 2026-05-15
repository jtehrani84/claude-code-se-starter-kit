#!/usr/bin/env python3
"""
LLMGW Review Caller — Routes documents to external models for adversarial QA.
Uses Salesforce LLM Gateway (LiteLLM proxy → Bedrock).
Requires ZScaler VPN active.
"""

import json
import sys
import os
import urllib.request
import urllib.error
from pathlib import Path

# Reads gateway URL from env vars set by Claude Code + LLMGW installer.
# ANTHROPIC_BEDROCK_BASE_URL includes /bedrock suffix — strip it for direct calls.
# Fallback: LLMGW_BASE_URL if set explicitly.
GATEWAY_BASE = os.environ.get("ANTHROPIC_BEDROCK_BASE_URL", "").replace("/bedrock", "") or os.environ.get("LLMGW_BASE_URL", "")
MODELS = {
    "gpt-5.5": "gpt-5.5",
    "gpt-5": "gpt-5",
    "gemini-3.1-pro": "gemini-3.1-pro-preview",
    "gemini-2.5-pro": "gemini-2.5-pro",
    "gemini-flash": "gemini-3-flash-preview",
    "codex": "gpt-5.3-codex",
}
DEFAULT_EDITORIAL = "gemini-3.1-pro-preview"
DEFAULT_ADVERSARIAL = "gemini-3.1-pro-preview"  # GPT-5.5 returns empty on gateway. Use Gemini for both until fixed.

PROMPTS_DIR = Path(__file__).parent / "review-prompts"


def get_api_key():
    settings_path = Path.home() / ".claude" / "settings.json"
    if not settings_path.exists():
        print("ERROR: ~/.claude/settings.json not found", file=sys.stderr)
        sys.exit(1)
    with open(settings_path) as f:
        settings = json.load(f)
    key = settings.get("env", {}).get("ANTHROPIC_AUTH_TOKEN")
    if not key:
        print("ERROR: ANTHROPIC_AUTH_TOKEN not found in settings.json env", file=sys.stderr)
        sys.exit(1)
    return key


def load_prompt(mode):
    prompt_file = PROMPTS_DIR / f"{mode}.txt"
    if not prompt_file.exists():
        print(f"ERROR: Prompt template not found: {prompt_file}", file=sys.stderr)
        sys.exit(1)
    return prompt_file.read_text()


def call_llmgw(model_id, system_prompt, user_content, api_key):
    url = f"{GATEWAY_BASE}/v1/chat/completions"
    payload = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "max_tokens": 4096,
    }
    if not model_id.startswith("gpt-5") and not model_id.startswith("claude-opus-4-7"):
        payload["temperature"] = 0.3

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Content-Type", "application/json")

    try:
        resp = urllib.request.urlopen(req, timeout=120)
        result = json.loads(resp.read())
        return result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        body = e.read().decode() if e.fp else ""
        if e.code == 401:
            print("ERROR: Authentication failed. Is ZScaler VPN active?", file=sys.stderr)
        elif e.code == 400:
            print(f"ERROR: Bad request. Model '{model_id}' may not be available.\n{body}", file=sys.stderr)
        else:
            print(f"ERROR: HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: Connection failed. Is ZScaler VPN active?\n{e.reason}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


def detect_mode(file_path):
    path_str = str(file_path).lower()
    name = file_path.name.lower()

    if "stokes" in name or "competitive" in name or "positioning" in name or "strategy" in name:
        return "adversarial"
    if "email" in name or "slack" in name or "reply" in name:
        return "adversarial"
    if file_path.suffix == ".html" and ("deliverables" in path_str or "diagrams" in path_str):
        return "editorial"
    if file_path.suffix == ".md" and ("concepts" in path_str or "brief" in path_str):
        return "editorial"
    return "editorial"


def detect_model(mode):
    if mode == "adversarial":
        return DEFAULT_ADVERSARIAL
    return DEFAULT_EDITORIAL


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Review a document via LLMGW")
    parser.add_argument("file", help="Path to file to review")
    parser.add_argument("--model", choices=list(MODELS.keys()), help="Override model selection")
    parser.add_argument("--mode", choices=["editorial", "adversarial"], help="Override review mode")
    parser.add_argument("--list-models", action="store_true", help="List available models")

    args = parser.parse_args()

    if args.list_models:
        print("Available models on LLMGW:")
        for short, full in MODELS.items():
            marker = " (default editorial)" if full == DEFAULT_EDITORIAL else ""
            marker = " (default adversarial)" if full == DEFAULT_ADVERSARIAL else marker
            print(f"  {short:20s} → {full}{marker}")
        sys.exit(0)

    file_path = Path(args.file).resolve()
    if not file_path.exists():
        print(f"ERROR: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    content = file_path.read_text()
    if len(content) > 100000:
        print(f"WARNING: File is {len(content)} chars. Truncating to 100K for review.", file=sys.stderr)
        content = content[:100000]

    mode = args.mode or detect_mode(file_path)
    model_id = MODELS.get(args.model, detect_model(mode))

    system_prompt = load_prompt(mode)
    api_key = get_api_key()

    print(f"Reviewing: {file_path.name}")
    print(f"Mode: {mode} | Model: {model_id}")
    print(f"Sending to LLMGW...")
    print()

    response = call_llmgw(model_id, system_prompt, content, api_key)
    print(response)


if __name__ == "__main__":
    main()
