# /review — Multi-Model Adversarial Document Review

Route documents to external frontier models (GPT-5.5, Gemini 3.1 Pro) for adversarial QA via Salesforce LLMGW. Returns structured feedback categorized by severity.

## Usage

```
/review [file_path]                          # Auto-detect mode + model
/review [file_path] --adversarial            # Force adversarial (GPT-5.5)
/review [file_path] --editorial              # Force editorial (Gemini 3.1 Pro)
/review [file_path] --model gpt-5.5          # Force specific model
```

## What to Do

1. Read the file at the specified path (or ask the user which file to review)
2. Run the LLMGW review script:
   ```bash
   python3 ~/.claude/hooks/scripts/llmgw-review.py [FILE_PATH] [--mode MODE] [--model MODEL]
   ```
3. Display the structured findings to the user
4. For each finding, evaluate whether it's valid given YOUR knowledge of the codebase:
   - If the external model flags something that contradicts source-verified facts → note it's INVALID and explain why
   - If the finding is valid → suggest how to fix it
   - If it's a judgment call → present both sides

## Model Selection (Auto-Detect)

| Content Pattern | Mode | Model | Why |
|---|---|---|---|
| `stokes-*`, `*-competitive-*`, `*-strategy-*`, exec emails | adversarial | GPT-5.5 | Simulates skeptical buyer |
| Deliverable HTML, briefs, wiki concepts, demo scripts | editorial | Gemini 3.1 Pro | Structural editor + reader empathy |
| Override with --model or --mode anytime | | | |

## Critical Rules

- **NEVER auto-apply findings.** Present them. Let the user decide.
- **Evaluate against codebase context.** The external model doesn't have source access. Some findings will be wrong because the reviewer doesn't know what we've verified.
- **Flag when external model is wrong.** If GPT-5.5 challenges a claim that we source-verified, say so explicitly: "This finding is INVALID — we verified X against SOURCE-AUDIT-MGR.md."
- **Don't send sensitive data.** No customer names, account IDs, deal values, or internal Salesforce code through the gateway. Documents only.

## Available Models

Run `python3 ~/.claude/hooks/scripts/llmgw-review.py --list-models` to see current options.

## Requirements

- ZScaler VPN must be active (same requirement as Claude Code itself)
- ANTHROPIC_AUTH_TOKEN must be set in ~/.claude/settings.json (set by LLMGW installer)
