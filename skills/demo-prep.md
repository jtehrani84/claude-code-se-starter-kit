# /demo-prep

Generate a demo script from account context. What to show, what to say, and what to skip.

## Trigger
When the user says: "demo prep", "prep demo for [company]", "demo script", "what should I show [company]"

## Workflow

1. **Identify:** Which account? What products? Who's in the room? What do they care about?
2. **Build the script:**

### Output Format

```
## Demo Script: [Company] — [Date]
**Audience:** [Names + Roles]
**Duration:** [X minutes]
**Their Priority:** [The ONE thing they need to see solved]

### Opening (2 minutes)
**Say:** "[Question about their specific challenge — NOT 'let me show you Salesforce']"
**Goal:** Confirm the problem. Make them nod.

### Act 1: Their Problem, Solved ([X] minutes)
**Show:** [Specific screen/flow that addresses their #1 priority]
**Say:** "[How this connects to the metric they mentioned]"
**Skip:** [What NOT to show — features that distract from the narrative]

### Act 2: The Multiplier ([X] minutes)
**Show:** [The second capability that makes Act 1 more powerful]
**Say:** "[How this compounds the value — connect to their scale/team/timeline]"
**Transition:** "[Bridge question: 'How does your team handle X today?']"

### Act 3: The Future ([X] minutes)
**Show:** [What becomes possible next — roadmap or advanced capability]
**Say:** "[Vision statement in THEIR language, not ours]"

### Close (2 minutes)
**Ask:** "[Specific next step — not 'thoughts?']"
**Fallback:** "[If they push back, pivot to THIS]"

### Landmines to Avoid
- [Topic/feature NOT to bring up and why]
- [Competitive claim NOT to make]
- [Technical limitation to sidestep]

### If They Ask About...
| Question | Answer |
|----------|--------|
| [Likely question #1] | [Concise response] |
| [Likely question #2] | [Concise response] |
| [Competitor comparison] | [Honest positioning] |
```

## Rules
- NEVER start a demo with "Let me show you Salesforce" — start with THEIR problem
- The demo is a story about THEM, not a product tour
- Skip features that don't connect to their stated priorities
- Include landmines — what NOT to show is as important as what to show
- If you don't know their priorities, say so and suggest discovery questions first
- Keep total script under 600 words
