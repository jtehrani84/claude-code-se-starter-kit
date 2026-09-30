#!/usr/bin/env python3
"""
LLMGW Multi-Model Caller — Routes prompts to any model on Salesforce LLMGW.

Usage:
  python3 llmgw-call.py --model haiku --prompt "Check this for errors"
  python3 llmgw-call.py --model sonnet --prompt "Validate" --file output.md
  python3 llmgw-call.py --model sol --prompt "Adversarial review" --file draft.md
  python3 llmgw-call.py --list-models

Available models (live-verified 2026-09-29; the gateway catalog changes, re-run --list-models against
a live call before relying on an id):
  Claude: claude-opus-5-5, claude-sonnet-5-5, claude-sonnet-5, claude-opus-4-8, claude-haiku-4-5-20251001, ...
  GPT:    gpt-5.6, gpt-5.6-sol, gpt-5.6-luna, gpt-5.6-terra, gpt-5.5, gpt-5, gpt-5-mini, gpt-4o, gpt-4o-mini
  Gemini: gemini-3.1-pro-preview, gemini-3-flash-preview, gemini-3.5-flash, gemini-3.7-flash, gemini-2.5-pro, gemini-2.5-flash
  xAI:    grok-4.6 (a thinking model: give it max_tokens >= 400 or the answer can come back empty)

Auth: uses ANTHROPIC_AUTH_TOKEN if set, else ~/.claude/settings.json env, else the DevBar CLI
(`devbar auth claude`), which is how most DevBar-managed installs authenticate.

Output: JSON with {model, content, usage} or plain text with --plain flag.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

LLMGW_BASE = os.environ.get("ANTHROPIC_BEDROCK_BASE_URL", "").replace("/bedrock", "") or os.environ.get("LLMGW_BASE_URL", "")


def resolve_token() -> str:
    """Env var, then settings.json env, then the DevBar CLI. Returns '' if none work."""
    tok = os.environ.get("ANTHROPIC_AUTH_TOKEN", "")
    if tok:
        return tok
    try:
        settings = json.loads((Path.home() / ".claude" / "settings.json").read_text())
        tok = settings.get("env", {}).get("ANTHROPIC_AUTH_TOKEN", "")
        if tok:
            return tok
    except Exception:
        pass
    devbar = shutil.which("devbar") or "/Applications/devbar.app/Contents/MacOS/devbar"
    if os.path.exists(devbar):
        try:
            out = subprocess.run([devbar, "auth", "claude"], capture_output=True, text=True, timeout=20)
            return out.stdout.strip() if out.returncode == 0 else ""
        except Exception:
            return ""
    return ""


TOKEN = resolve_token()

ANTHROPIC_MODELS = {
    "claude-opus-5-5", "claude-sonnet-5-5", "claude-sonnet-5", "claude-opus-4-8", "claude-opus-4-7",
    "claude-opus-4-6-v1", "claude-opus-4-5-20251101", "claude-sonnet-4-6", "claude-sonnet-4-5-20250929",
    "claude-sonnet-4-20250514", "claude-haiku-4-5-20251001",
}

ALL_MODELS = ANTHROPIC_MODELS | {
    "gpt-5.6", "gpt-5.6-sol", "gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.5", "gpt-5", "gpt-5-mini", "gpt-4o", "gpt-4o-mini",
    "gemini-3.1-pro-preview", "gemini-3-flash-preview", "gemini-3.5-flash", "gemini-3.7-flash",
    "gemini-2.5-pro", "gemini-2.5-flash",
    "grok-4.6",
}

# Minimum output budget per model. Grok spends most of it thinking on long input (measured
# 2026-09-30: ~12K thinking tokens, then an ~8K-character answer, 146s, on a 21 KB document).
MIN_MAX_TOKENS = {"grok-4.6": 32000}

# Model aliases for convenience
ALIASES = {
    "haiku": "claude-haiku-4-5-20251001",
    "sonnet": "claude-sonnet-5-5",
    "opus": "claude-opus-5-5",
    "opus48": "claude-opus-4-8",
    "sol": "gpt-5.6-sol",
    "luna": "gpt-5.6-luna",
    "terra": "gpt-5.6-terra",
    "gpt5": "gpt-5",
    "gpt55": "gpt-5.5",
    "gemini": "gemini-3.1-pro-preview",
    "flash": "gemini-3.5-flash",
    "grok": "grok-4.6",
}


def call_model(model: str, prompt: str, system: str = "", max_tokens: int = 4096, timeout: int = 600) -> dict:
    """Call any model via LLMGW Messages API."""
    resolved = ALIASES.get(model, model)
    if resolved not in ALL_MODELS:
        return {"error": f"Unknown model: {resolved}. Use --list-models to see available."}
    # Grok thinks before it answers, and the gateway has no way to cap that (it rejects thinking and
    # reasoning_effort params). On a long document it can spend 12K+ tokens thinking, so a smaller
    # budget comes back with no answer at all. It stops early on short prompts, so the floor is cheap.
    floor = MIN_MAX_TOKENS.get(resolved, 0)
    if max_tokens < floor:
        max_tokens = floor

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
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode() if e.fp else str(e)
        return {"error": f"HTTP {e.code}: {error_body}", "model": resolved}
    except Exception as e:
        msg = str(e)
        if "timed out" in msg:
            msg += f" (no reply within {timeout}s; thinking models can take minutes on long input, raise --timeout)"
        return {"error": msg, "model": resolved}

    # Normalize response across API formats
    if "content" in data:
        # Anthropic Messages API format. Thinking models (e.g. Grok) put a thinking or
        # redacted_thinking block first, so join every text block rather than reading [0].
        text = "".join(b.get("text", "") for b in (data["content"] or []) if b.get("type") == "text")
        usage = data.get("usage", {})
    elif "choices" in data:
        # OpenAI format
        text = data["choices"][0].get("message", {}).get("content", "")
        usage = data.get("usage", {})
    else:
        text = json.dumps(data)
        usage = {}

    stop = data.get("stop_reason") or (data.get("choices") or [{}])[0].get("finish_reason")
    if not text.strip():
        why = f"it hit max_tokens={max_tokens} while thinking; raise --max-tokens" if stop in ("max_tokens", "length") else f"stop reason: {stop}"
        return {"error": f"{resolved} returned an empty answer ({why})", "model": resolved, "usage": usage}

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
    parser.add_argument("--timeout", type=int, default=600, help="Seconds to wait for a reply (default 600)")
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
        print("\nxAI:")
        for m in sorted(m for m in ALL_MODELS if m.startswith("grok")):
            alias = next((k for k, v in ALIASES.items() if v == m), "")
            print(f"  {m}" + (f" ({alias})" if alias else ""))
        return

    if not args.prompt:
        parser.error("--prompt is required (or use --list-models)")

    if not TOKEN:
        print(json.dumps({"error": "No LLMGW token found. Set ANTHROPIC_AUTH_TOKEN, or sign in to DevBar (devbar auth claude)."}))
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

    result = call_model(args.model, prompt, args.system, args.max_tokens, args.timeout)

    # An error must never look like an answer: it goes to stderr with a nonzero exit.
    if "error" in result:
        print(f"ERROR: {result['error']}", file=sys.stderr)
        if not args.plain:
            print(json.dumps(result, indent=2))
        sys.exit(1)
    if args.plain:
        print(result["content"])
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
