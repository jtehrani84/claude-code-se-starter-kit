# /validate

Cross-model quality gate. Routes content through independent validation before shipping.

## Trigger
When the user says: "validate this", "quality check", "is this ready to send?", "validate [file]", "second opinion on this"

## Workflow

### 1. Identify the content
If a file path is provided, read it. Otherwise, use the last substantive output from this session.

### 2. Run validation checks

Score each dimension 1-10:

**Factual Accuracy**
- Are all claims verifiable?
- Are product names correct? (Check against salesforce.com if Salesforce-related)
- Are numbers, dates, and statistics sourced?
- Any fabricated quotes, case studies, or customer references?

**Voice Quality**
- Scan for banned AI-slop words (the full 50+ word list)
- Check for banned phrases and structures
- Does it sound like a real person wrote it?
- Would you say this out loud without cringing?

**Specificity**
- Numbers over adjectives? ("34M users" not "massive user base")
- Named examples over generic claims?
- Concrete next steps over vague suggestions?

**Customer Centricity**
- Does it lead with their world, not ours?
- 70/30 ratio (their priorities vs our products)?
- Are their metrics and KPIs referenced, not ours?

**Actionability**
- Is there a clear next step?
- Does the reader know what to do after reading this?
- Is there a specific date, time, or owner for the action?

**Credibility**
- Would you send this to a C-suite executive?
- Would your VP forward this without editing?
- Does it demonstrate expertise or just awareness?

### 3. Produce the report

```
## Validation Report

**Content:** [file name or description]
**Word count:** [X]

| Dimension | Score | Issue |
|-----------|-------|-------|
| Accuracy | X/10 | [brief note if <8] |
| Voice | X/10 | [brief note if <8] |
| Specificity | X/10 | [brief note if <8] |
| Customer Focus | X/10 | [brief note if <8] |
| Actionability | X/10 | [brief note if <8] |
| Credibility | X/10 | [brief note if <8] |

**Overall: X/10**

### Critical Issues
- [List anything that must be fixed before shipping]

### Suggestions
- [Optional improvements, not blockers]

### Verdict: [SHIP / FIX FIRST / REWRITE]
```

**Verdict thresholds:**
- SHIP: Overall 8+ and no dimension below 6
- FIX FIRST: Overall 6-7, or any dimension below 5
- REWRITE: Overall below 6, or Accuracy below 5

### 4. If FIX FIRST or REWRITE
Offer to fix the issues immediately. List the specific changes needed.

## Rules
- Never rubber-stamp content. If it's genuinely good, say so with specifics about WHY.
- Flag hallucinated product names as Critical (not just a suggestion)
- A single banned word is a voice violation — flag it even if everything else is perfect
- "Would you send this to a C-suite exec?" is the ultimate bar
- If content is internal-only (memo, notes), relax Credibility to 6+ threshold
