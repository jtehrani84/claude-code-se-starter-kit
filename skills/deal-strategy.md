# /deal-strategy

Generate a tactical deal strategy for a specific opportunity. Combines account context, competitive positioning, and talk tracks.

## Trigger
When the user says: "deal strategy", "strategy for [company]", "how do I win [deal]", "competitive positioning for [company]"

## Workflow

1. **Identify the opportunity** — company, product interest, stage, competitors
2. **Analyze the landscape:**
   - What's the customer trying to solve?
   - Who are we competing against?
   - What's our differentiation?
   - What's the urgency driver (why now)?
3. **Build the strategy:**

### Output Format

```
## Deal Strategy: [Company] — [Opportunity Name]

### Situation (2 sentences)
[What the customer needs and why they're evaluating now]

### Competitive Landscape
| Competitor | Their Pitch | Our Counter |
|-----------|------------|-------------|
| [Name] | [Their angle] | [Why we win] |

### Why Us (3 bullets max)
1. [Strongest differentiator for THIS customer]
2. [Second strongest]
3. [Third — if it exists]

### Why Now (urgency driver)
[The business event or timeline forcing a decision — NOT Salesforce contract timing]

### Talk Track
**Opening:** "[Question that surfaces their pain]"
**Bridge:** "[How their pain connects to our capability]"
**Proof:** "[Reference customer or metric]"
**Close:** "[Specific next step with date]"

### Risks & Mitigation
- Risk: [biggest deal risk]
  Mitigation: [what to do about it]

### Recommended Next Steps
1. [Action] — by [date]
2. [Action] — by [date]
```

## Rules
- NEVER use Salesforce contract end-dates as "Why Now" — customers see through it
- Why Now must be THEIR business driver (regulation, board mandate, competitive pressure, growth target)
- Competitive counters must be factual — never trash-talk
- If you don't know the competitor, say so and suggest discovery questions
- Keep total output under 500 words
