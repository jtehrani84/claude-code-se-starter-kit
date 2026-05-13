Generate a per-persona strategic engagement playbook for a target account. Transforms account research into an executable, team-ready playbook with orchestration cadence, conversation prompts, objection matrices, and stakeholder mapping.

Takes an account name as argument.

Examples:
- `/engagement-playbook Acme Corp`
- `/engagement-playbook "Global Industries"`

## Prerequisites
- Run `/account-prep [company]` first if you haven't already gathered intelligence
- Or provide context about the account in your message

## Workflow

### 1. Gather Intelligence

#### 1a. Check existing context
- Search wiki/people/ for any entity pages on contacts at this account
- Search memory for prior interactions or deal history
- Check wiki for any existing account pages

#### 1b. Web research
Search for:
- Recent company news (earnings, leadership changes, tech initiatives)
- Technology stack and current vendors
- Industry trends affecting them
- Hiring signals (AI, automation, platform roles)

#### 1c. CRM data (if available)
If you have CRM access (Salesforce CLI, MCP, or other):
- Open opportunities with stage and close date
- Key contacts and their roles
- Contract history and current products
- Lost deal history (critical for objection prep)

### 2. Stakeholder Mapping

For each identified persona, determine:
- **Decision authority:** Economic buyer, technical evaluator, champion, or blocker
- **Priority:** What they care about most (from their role + company context)
- **Communication style:** Data-driven, relationship-driven, speed-driven
- **Entry point:** Best first conversation topic

### 3. Build the Playbook

Output this structure:

```markdown
## [Account Name] — Engagement Playbook
**Generated:** [date]
**Deal Stage:** [if known]
**Primary Objective:** [what we're trying to achieve]

### Account Snapshot
- Industry: [X] | Employees: [X] | Revenue: [X]
- Recent signal: [what triggered this engagement]
- Competitive landscape: [who else is in play]
- Current technology: [what they run today]
- Contract status: [existing customer? net-new? expansion?]

### Stakeholder Map
| Name | Title | Role in Deal | Top Priority | Approach |
|------|-------|-------------|-------------|----------|
| [name] | [title] | Economic Buyer | [their priority] | [how to engage] |
| [name] | [title] | Technical Evaluator | [their priority] | [how to engage] |
| [name] | [title] | Champion | [their priority] | [how to engage] |

### Per-Persona Engagement Plan

#### [Persona 1 — Title]
**What they care about:** [specific, not generic]
**Opening move:** [first email or conversation starter]
**Value message:** [one sentence, their language, their metrics]
**Objection to prepare for:** [most likely pushback based on role]
**Proof point:** [reference customer, stat, or demo to use]
**Cadence:** [how often, what channel — email, Slack, meeting]

#### [Persona 2 — Title]
[Same structure]

### Orchestration Timeline
| Week | Action | Owner | Milestone |
|------|--------|-------|-----------|
| 1 | [first touch] | [who] | Initial contact |
| 2 | [follow-up] | [who] | Discovery scheduled |
| 3 | [demo/POV] | [who] | Technical validation |
| 4 | [proposal] | [who] | Decision checkpoint |

### Objection Matrix
| Objection | Response Framework | Proof Point | When It Comes Up |
|-----------|-------------------|-------------|-----------------|
| "We already have [competitor]" | [approach] | [evidence] | Discovery |
| "Budget isn't approved" | [approach] | [evidence] | Proposal |
| "Not a priority right now" | [approach] | [evidence] | Initial touch |

### Competitive Positioning
| Competitor | Their Strength | Our Angle | Differentiator |
|-----------|---------------|-----------|----------------|
| [name] | [what they do well] | [where we win] | [proof] |

### Next Best Action
**This week:** [single most important action to take RIGHT NOW]
**If they go dark:** [re-engagement strategy]
**Escalation trigger:** [when to bring in leadership]
```

## Rules

- 70% their world, 30% our capabilities — always lead with their business outcomes
- Every claim needs a proof point or "needs discovery" flag
- Stakeholder priorities must come from real signals (news, hiring, earnings) not generic role assumptions
- Playbook must be actionable THIS WEEK — not a 90-day strategy doc no one reads
- If data is insufficient, say "needs discovery" rather than fabricating context
- Include lost deal history if available — the objection that killed the last deal will come back
- Never use "leverage", "ecosystem", "unlock", "empower" or other banned AI-slop words
- Keep total output under 1000 words unless user asks for more detail
- All stats must be sourced — never fabricate customer metrics or market data

## After Generation

1. Save to wiki or a local playbooks directory for future reference
2. Suggest: "Run `/post-meeting` after your first interaction to update the timeline"
3. If entity pages exist for contacts mentioned, suggest appending engagement plan context
