# /review — Multi-Model Adversarial Document Review

Route documents to frontier models from a **different lab than the one that drafted them** (OpenAI's GPT-5.6 Sol, Google's Gemini 3.1 Pro, xAI's Grok) for adversarial QA via Salesforce LLMGW. A same-model judge grades its own house style too kindly, so the reviewer is never Claude. Returns structured feedback categorized by severity.

## Usage

```
/review [file_path]                          # Auto-detect mode + model
/review [file_path] --adversarial            # Force adversarial (GPT-5.6 Sol)
/review [file_path] --editorial              # Force editorial (Gemini 3.1 Pro)
/review [file_path] --model grok             # Force a specific reviewer
```

## What to Do

1. Read the file at the specified path (or ask the user which file to review)
2. Run the LLMGW review script (installed by setup.sh):
   ```bash
   python3 ~/.claude/scripts/llmgw-review.py [FILE_PATH] [--mode MODE] [--model MODEL]
   ```
   If one reviewer times out or returns empty, re-run with another `--model`. The only rule is that it isn't the lab that wrote the draft.
3. Display the structured findings to the user
4. For each finding, evaluate whether it's valid given YOUR knowledge of the codebase:
   - If the external model flags something that contradicts source-verified facts → note it's INVALID and explain why
   - If the finding is valid → suggest how to fix it
   - If it's a judgment call → present both sides

## Model Selection (Auto-Detect)

| Content Pattern | Mode | Model | Why |
|---|---|---|---|
| `*-competitive-*`, `*-strategy-*`, exec emails | adversarial | GPT-5.6 Sol | Simulates a skeptical buyer, premium tier |
| Deliverable HTML, briefs, wiki concepts, demo scripts | editorial | Gemini 3.1 Pro | Structural editor + reader empathy |
| Override with --model or --mode anytime | | | |

## Critical Rules

- **NEVER auto-apply findings.** Present them. Let the user decide.
- **Make each finding earn its fix.** For code, a finding counts once it's a failing test. For prose, once you can point at the exact claim and the source it contradicts. A finding you can't reproduce gets dismissed with a reason, not obeyed.
- **Evaluate against codebase context.** The external model doesn't have source access. Some findings will be wrong because the reviewer doesn't know what we've verified.
- **Flag when the external model is wrong.** If a reviewer challenges a claim we source-verified, say so explicitly: "This finding is INVALID — we verified X against [source]."
- **Don't send sensitive data.** No customer names, account IDs, deal values, or internal Salesforce code through the gateway. Documents only.

## Available Models

Run `python3 ~/.claude/scripts/llmgw-review.py --list-models` to see current options. The gateway roster changes, so confirm with one live call before relying on a model.

## Requirements

- ZScaler VPN must be active (same requirement as Claude Code itself)
- An LLMGW token: the script uses `ANTHROPIC_AUTH_TOKEN` if set, then `~/.claude/settings.json`, then the DevBar CLI (`devbar auth claude`)
