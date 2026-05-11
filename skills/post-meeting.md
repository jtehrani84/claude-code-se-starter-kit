# /post-meeting

Capture meeting outcomes and fan out to all downstream systems. One input (your notes), five outputs.

## Trigger
When the user says: "post meeting", "meeting notes", "capture meeting", "debrief [company]"

## Workflow

1. **Collect raw notes** — ask what happened, key takeaways, commitments made
2. **Generate all outputs:**

### Output Format

```
## Post-Meeting Capture: [Company] — [Date]

### Key Takeaways (3 bullets max)
1. [Most important thing learned]
2. [Second most important]
3. [Third — if applicable]

### Commitments Made
| Who | What | By When |
|-----|------|---------|
| [Name] | [Action] | [Date] |

### Follow-Up Email Draft
Subject: [Specific reference to something discussed]

[2-3 sentences max. Reference ONE specific moment from the conversation.
Confirm action items. Propose next meeting with specific date. Under 150 words.]

[Your Name], [Title], Salesforce

### CRM Update (copy to Salesforce)
**Activity Type:** Meeting
**Subject:** [Meeting topic]
**Description:** [3-sentence summary: what was discussed, what was decided, what's next]
**Next Step:** [Specific action with date]

### Memory Save (if applicable)
[Anything Claude should remember for future interactions with this account:
- Key stakeholder preferences or communication style
- Technical requirements or constraints mentioned
- Competitive intel shared
- Decision timeline or budget signals]
```

## Rules
- Send follow-up within 2 hours of the meeting
- Reference ONE specific moment from the conversation (proves you were present)
- Every commitment needs an owner AND a date
- If the customer said something that changes strategy, flag it explicitly
- CRM update should be paste-ready for Salesforce Activity
- Memory save only for non-obvious information (not what's in the CRM)
