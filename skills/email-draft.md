# /email-draft

Draft a customer or internal email that passes the anti-slop test. No AI voice. No filler. Under 200 words.

## Trigger
When the user says: "draft email", "email to [person]", "write an email", "follow up email"

## Workflow

1. **Clarify:** Who is the recipient? What's the ask? What context do they need?
2. **Draft** following the rules below
3. **Self-check** against banned patterns before presenting

### Output Format

```
Subject: [Specific, under 10 words — no generic "Follow Up" or "Quick Question"]

[Body — under 200 words, starting with substance]

[Sign-off]
[Your Name], [Title], Salesforce
```

## Rules

### Structure
- Start with a specific fact, reference, or number — NEVER a pleasantry
- One specific ask with a suggested date/time
- End with the next step, not "let me know"
- Under 200 words total

### Tone Matching
- C-suite: strategic, concise, bold claims backed by data
- VP/Director: tactical, outcome-focused, specific timelines
- Technical: precise product names, architecture-aware, honest about tradeoffs
- Peer/internal: direct, candid, no ceremony

### Banned (instant fail)
- "I hope this finds you well"
- "Per our conversation"
- "Please don't hesitate to reach out"
- "Just circling back"
- "Wanted to touch base"
- "Best regards" / "Warm regards" (just "Best," or "Thanks,")
- Any word from the anti-slop banned list

### Quality Check
Before presenting the draft, verify:
- [ ] Starts with substance (not a greeting)
- [ ] Has exactly one ask
- [ ] Under 200 words
- [ ] No banned words or phrases
- [ ] Tone matches recipient seniority
- [ ] Ends with a specific next step
