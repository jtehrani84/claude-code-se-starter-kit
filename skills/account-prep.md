# /account-prep

Pre-meeting intelligence gathering. Run before any customer meeting to have structured context.

## Trigger
When the user says: "account prep", "prep for meeting", "prep for [company]", "meeting with [company]"

## Workflow

1. **Identify the account** — ask if not provided
2. **Gather intelligence:**
   - Company overview (size, industry, recent news)
   - Salesforce relationship history (if CRM access available)
   - Recent deals, open opportunities, key contacts
   - Competitive landscape for this account
   - Industry trends affecting them
3. **Structure the output:**

### Output Format

```
## [Company Name] — Meeting Prep
**Date:** [meeting date if known]
**Attendees:** [if known]

### Company Snapshot
- Industry: [X] | Size: [X employees] | Revenue: [X]
- Recent news: [1-2 relevant headlines]

### Salesforce Relationship
- Account owner: [name]
- Open opportunities: [list with stage]
- Last meaningful interaction: [date + summary]
- Key contacts: [names + roles]

### Their World (What They Care About)
- [Top business priority #1]
- [Top business priority #2]
- [Relevant challenge or initiative]

### Our Angle
- [Which Salesforce capability maps to their priorities]
- [Proof point or reference story]
- [Potential expansion area]

### Meeting Agenda Suggestion
1. [Opening question — about THEM, not us]
2. [Discovery area]
3. [Value demonstration point]
4. [Next step to propose]
```

## Rules
- 70% their world, 30% Salesforce
- Lead with THEIR metrics, not our product names
- Include a specific opening question that proves you did homework
- If data is unavailable, say so — never fabricate
- Keep total output under 400 words
