#!/usr/bin/env python3
"""
LLMGW Multi-Model Caller — Routes prompts to any model on Salesforce LLMGW.

Usage:
  python3 llmgw-call.py --model claude-haiku-4-5-20251001 --prompt "Check this for errors"
  python3 llmgw-call.py --model claude-sonnet-4-6 --prompt "Validate" --file output.md
  python3 llmgw-call.py --model gpt-5.5 --prompt "Alternative framing" --file draft.md
  python3 llmgw-call.py --list-models

Available models (confirmed 2026-05-10):
  Claude: claude-haiku-4-5-20251001, claude-sonnet-4-6, claude-opus-4-6-v1, claude-opus-4-7
  GPT: gpt-4o, gpt-4o-mini, gpt-5, gpt-5-mini, gpt-5.5, gpt-5.2-codex, gpt-5.3-codex
  Gemini: gemini-2.0-flash, gemini-2.5-pro, gemini-2.5-flash, gemini-3-pro-preview, gemini-3-flash-preview, gemini-3.1-pro-preview

Output: JSON with {model, content, usage} or plain text with --plain flag.
"""

import argparse
import json
import os
import sys
import urllib.request

LLMGW_BASE = os.environ.get("ANTHROPIC_BEDROCK_BASE_URL", "").replace("/bedrock", "") or os.environ.get("LLMGW_BASE_URL", "")
TOKEN = os.environ.get("ANTHROPIC_AUTH_TOKEN", "")

ANTHROPIC_MODELS = {
    "claude-haiku-4-5-20251001", "claude-sonnet-4-20250514", "claude-sonnet-4-5-20250929",
    "claude-sonnet-4-6", "claude-opus-4-5-20251101", "claude-opus-4-6-v1", "claude-opus-4-7"
}

ALL_MODELS = ANTHROPIC_MODELS | {
    "gemini-2.0-flash", "gemini-2.5-pro", "gemini-2.5-flash",
    "gemini-3-pro-preview", "gemini-3-flash-preview", "gemini-3.1-pro-preview",
    "gpt-4o", "gpt-4o-mini", "gpt-5", "gpt-5-mini", "gpt-5.5", "gpt-5.2-codex", "gpt-5.3-codex"
}

# Model aliases for convenience
ALIASES = {
    "haiku": "claude-haiku-4-5-20251001",
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-6-v1",
    "opus47": "claude-opus-4-7",
    "gpt5": "gpt-5",
    "gpt55": "gpt-5.5",
    "gemini": "gemini-2.5-pro",
    "flash": "gemini-2.5-flash",
}


def call_model(model: str, prompt: str, system: str = "", max_tokens: int = 4096) -> dict:
    """Call any model via LLMGW Messages API."""
    resolved = ALIASES.get(model, model)
    if resolved not in ALL_MODELS:
        return {"error": f"Unknown model: {resolved}. Use --list-models to see available."}

    messages = [{"role": "user", "content": prompt}]

    body = {
        "model": resolved,
        "max_tokens": max_tokens,
        "messages": messages,
    }
    if system:
        body["system"] = system

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
        "anthropic-version": "2023-06-01",
    }

    req = urllib.request.Request(
        f"{LLMGW_BASE}/v1/messages",
        data=json.dumps(body).encode(),
        headers=headers,
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode() if e.fp else str(e)
        return {"error": f"HTTP {e.code}: {error_body}", "model": resolved}
    except Exception as e:
        return {"error": str(e), "model": resolved}

    # Normalize response across API formats
    if "content" in data:
        # Anthropic Messages API format
        text = data["content"][0]["text"] if data["content"] else ""
        usage = data.get("usage", {})
    elif "choices" in data:
        # OpenAI format
        text = data["choices"][0].get("message", {}).get("content", "")
        usage = data.get("usage", {})
    else:
        text = json.dumps(data)
        usage = {}

    return {
        "model": resolved,
        "content": text,
        "usage": usage,
    }


def main():
    parser = argparse.ArgumentParser(description="Call any LLMGW model")
    parser.add_argument("--model", "-m", default="haiku", help="Model name or alias")
    parser.add_argument("--prompt", "-p", required=False, help="User prompt")
    parser.add_argument("--system", "-s", default="", help="System prompt")
    parser.add_argument("--file", "-f", help="File to include in prompt context")
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--plain", action="store_true", help="Output text only, no JSON wrapper")
    parser.add_argument("--list-models", action="store_true", help="List available models")
    args = parser.parse_args()

    if args.list_models:
        print("Available models (aliases in parens):")
        print("\nClaude:")
        for m in sorted(ANTHROPIC_MODELS):
            alias = next((k for k, v in ALIASES.items() if v == m), "")
            print(f"  {m}" + (f" ({alias})" if alias else ""))
        print("\nGPT:")
        for m in sorted(m for m in ALL_MODELS if m.startswith("gpt")):
            alias = next((k for k, v in ALIASES.items() if v == m), "")
            print(f"  {m}" + (f" ({alias})" if alias else ""))
        print("\nGemini:")
        for m in sorted(m for m in ALL_MODELS if m.startswith("gemini")):
            alias = next((k for k, v in ALIASES.items() if v == m), "")
            print(f"  {m}" + (f" ({alias})" if alias else ""))
        return

    if not args.prompt:
        parser.error("--prompt is required (or use --list-models)")

    if not TOKEN:
        print(json.dumps({"error": "ANTHROPIC_AUTH_TOKEN not set"}))
        sys.exit(1)

    prompt = args.prompt
    if args.file:
        try:
            with open(os.path.expanduser(args.file)) as f:
                file_content = f.read()
            prompt = f"{prompt}\n\n---\nFile content ({args.file}):\n{file_content}"
        except FileNotFoundError:
            print(json.dumps({"error": f"File not found: {args.file}"}))
            sys.exit(1)

    result = call_model(args.model, prompt, args.system, args.max_tokens)

    if args.plain:
        print(result.get("content", result.get("error", "")))
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
