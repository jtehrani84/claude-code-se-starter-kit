# What You Get — Complete Inventory

Everything in this kit, what it does, why it's here, and how it helps you.

---

## Rules (8 files) — Standards enforced every session

Rules load automatically on every Claude Code session. You never need to remind Claude of these — they fire silently in the background.

| File | What It Does | Why It's Here |
|------|-------------|---------------|
| `communication.md` | Enforces SE voice: no AI-slop (50+ banned words), email under 200 words, customer-centric framing | Every email, deck, and talk track sounds like YOU wrote it, not a chatbot |
| `security-governance.md` | CRUD/FLS checks, sharing model awareness, secrets handling, security review checklist | Claude never generates insecure code or exposes sensitive data |
| `architecture.md` | Decision framework, preferred patterns, anti-patterns, change design documentation | Architecture decisions are consistent and well-reasoned |
| `agent-script.md` | Agentforce/Agent Script conventions and patterns | Correct agent authoring from Day 1 |
| `salesforce-instructions.md` | Senior SF SE persona, platform-first approach, inspect metadata before proposing | Claude acts like an experienced Salesforce Solutions Engineer |
| `salesforce-platform.md` | Bulk-safe Apex, thin triggers, one trigger per object, LWC best practices, named credentials | Production-quality Salesforce code that passes code review |
| `testing-quality.md` | Realistic test data, meaningful assertions (not just coverage), quality gate mindset | Tests that actually catch bugs, not just hit coverage numbers |
| `slds2-lwc-ui.md` | SLDS 2 styling hooks, token migration, no hardcoded CSS values | Modern, compliant Lightning Web Components |

---

## Hooks (6 scripts) — Automated enforcement that can't be forgotten

Hooks run mechanically — before or after Claude takes an action. Unlike rules (which Claude reads and can forget in long conversations), hooks execute as code. They intercept mistakes at the moment of action.

| File | When It Fires | What It Does | Why It's Here |
|------|--------------|-------------|---------------|
| `session-init.py` | Session start | Routes relevant wiki pages, surfaces recent work, shows nudges | Every session starts with context — no "where was I?" |
| `guardrail.py` | Before Edit/Write | Blocks unsafe architecture patterns before code is written | Prevents infrastructure violations at point of action |
| `product-verification.py` | Before Edit/Write | Catches hallucinated Salesforce product names, suggests corrections | No more "Einstein Copilot" or "Agentforce Script" in customer content |
| `output-quality-gate.py` | After Write | Scans .md/.html files for 50+ banned AI-slop words, reports exact line numbers | Content quality is enforced mechanically, not by memory |
| `graph-auto-index.py` | After Write/Edit | Indexes entities into SQLite knowledge graph, computes relationship edges | Your knowledge graph grows automatically from your work |
| `soql-schema-check.py` | Before SOQL execution | Validates field names against org schema before running queries | Catches bad SOQL before it fails in the org |

---

## Skills (22 commands) — Workflows compressed into single commands

Each skill replaces 15-60 minutes of manual work. Say the command, get the output.

### Core SE Workflows (7)

| Skill | What It Does | Time Saved |
|-------|-------------|-----------|
| `/account-prep` | Full pre-meeting intelligence: company + CRM + competitive + suggested agenda | 30 min → 2 min |
| `/deal-strategy` | Competitive positioning + talk track + objection handling for a specific deal | 45 min → 3 min |
| `/email-draft` | Customer email with anti-slop, under 200 words, seniority-matched tone | 15 min → 30 sec |
| `/post-meeting` | Capture outcomes, action items, CRM update draft, follow-up email | 20 min → 2 min |
| `/demo-prep` | Demo script from account context, persona-driven delivery coaching | 30 min → 3 min |
| `/engagement-playbook` | Per-persona strategic playbook with stakeholder map and objection matrix | 60 min → 5 min |
| `/solution-design` | Solution architecture for customer deals with branded deliverables | 2 hrs → 15 min |

### Quality Assurance (3)

| Skill | What It Does | Time Saved |
|-------|-------------|-----------|
| `/validate` | Cross-model quality gate: 5 dimensions, SHIP/FIX/REWRITE verdict | Manual review → automated |
| `/voice-check` | Anti-slop scanner: full 50+ word banned list, replacements, pass/fail | Catches what you'd miss |
| `/content-review` | 6-dimension universal reviewer with scoring rubric (accuracy, voice, specificity, customer-centricity, actionability, credibility) | Peer review → instant |

### Intelligence & Growth (5)

| Skill | What It Does | Time Saved |
|-------|-------------|-----------|
| `/morning-brief` | Daily context: overnight intel, git status, memory changes, suggested actions | 15 min orientation → instant |
| `/scan-intel` | Daily intelligence sweep: web + social → categorized with ADOPT/EVALUATE/WATCH | 30 min research → 3 min |
| `/ingest` | Process any new source (PDF, URL, doc) into wiki pages with entity extraction | Manual notes → structured knowledge |
| `/week-plan` | Weekly planning: deals + intel + projects + priorities + blockers | 30 min planning → 5 min |
| `/weekly-report` | Status report from git + memory + wiki activity | Manual tracking → automated |

### System Maintenance (4)

| Skill | What It Does | Time Saved |
|-------|-------------|-----------|
| `/curate` | Memory maintenance: staleness scan, promotion, inbox processing, orphan detection | Knowledge base stays healthy without manual review |
| `/wiki-lint` | Wiki health check: orphans, dead links, stale pages, broken structure | Wiki stays trustworthy |
| `/system-health` | System diagnostics: hooks firing, rules loading, graph growing | Debug your setup |
| `/graph-query` | Query the knowledge graph: find relationships, connections, related files | "What do I know about X?" → instant |

### Compound Loop (2)

| Skill | What It Does | Time Saved |
|-------|-------------|-----------|
| `/skillify` | Meta-skill: do work → extract pattern → new permanent command. Skills build skills. | Manual skill authoring → automatic |
| `/context-load` | Cross-project context restore: load state from another project into current session | Context switching → instant |

### Code & Architecture (1)

| Skill | What It Does | Time Saved |
|-------|-------------|-----------|
| `/pr-review` | PR review against SF architecture and security standards | Manual review checklist → automated |

---

## Knowledge Graph (SQLite, auto-growing)

A local graph database that grows from your work. No external infrastructure — just Python + SQLite.

| Component | What It Does | How It Helps |
|-----------|-------------|-------------|
| `graph-auto-index.py` hook | Every Write/Edit indexes entities and computes relationships | Graph builds itself — zero maintenance |
| `graph-query` skill | Query relationships: "what relates to X?", "what mentions Y?" | Discover connections you didn't know existed |
| `wiki/entities/` | Company, product, concept pages indexed by the graph | Structured knowledge the graph can traverse |
| `wiki/people/` | Person pages with org trees and timelines | Relationship intelligence that compounds |

**How it compounds:** Write a memory about a deal. The hook indexes the account, people mentioned, and products discussed. Next time you prep for that account, the graph surfaces related wiki pages, other deals with the same people, and memory files you'd forgotten about. The more you write, the smarter retrieval gets.

---

## Passive Intelligence (Crons — overnight growth)

Your knowledge base grows while you sleep. These run on schedule without any manual effort.

| Script | Schedule | What It Does | How It Helps |
|--------|----------|-------------|-------------|
| `exa-scan.py` | Daily 4:30 AM | 5-query web intelligence (accounts, competitors, SF product, trends, Claude ecosystem) | Morning brief has fresh web intel |
| `hn-scan.py` | Daily 4:45 AM | 4-query Hacker News developer sentiment (free, no auth) | Know what developers are saying before customers mention it |
| `github-scan.py` | Daily 4:45 AM | Trending AI repos + release monitoring on competitor frameworks | What developers are actually adopting |
| `morning-digest.sh` | Daily 5:30 AM | Synthesizes all raw intel + Slack channels into wiki/inbox.md | One place to check each morning |
| `memory-decay-check.sh` | Weekly (Sunday) | Flags memory files unchanged >45 days | Catch stale knowledge before it misleads |
| `manage.sh` | Manual | Install/uninstall/status/test all crons | One command to manage the whole system |

---

## Wiki Structure (7 directories — ready to fill)

Pre-built directory structure so you never have to think about organization.

| Directory | What Goes Here | How It Grows |
|-----------|---------------|-------------|
| `wiki/concepts/` | Patterns, frameworks, competitive analysis, methodologies | From /ingest, /scan-intel, and manual capture |
| `wiki/entities/` | Companies, products, concepts (graph-indexed) | From /account-prep, /engagement-playbook, manual |
| `wiki/people/` | Person pages — internal and external contacts | From Slack profile seeding, /post-meeting |
| `wiki/projects/` | Project overviews and status | Manual — one page per active project |
| `wiki/tools/` | Tool documentation and setup guides | From /ingest when you learn a new tool |
| `wiki/events/` | Conference notes, event summaries | From /ingest after events |
| `wiki/insights/` | Research findings, analytical work | From /scan-intel ADOPT NOW items |
| `wiki/index.md` | Master catalog of all pages (Claude uses this to navigate) | Auto-updated when pages are added |
| `wiki/inbox.md` | Staging area for overnight intel and captures | Auto-populated by morning crons |

---

## Scripts (1)

| Script | What It Does | How It Helps |
|--------|-------------|-------------|
| `llmgw-call.py` | Universal multi-model API caller with aliases (haiku, sonnet, opus, gpt5, gemini) | Powers /validate for cross-model QA. Also callable from terminal for ad-hoc queries to any model. |

---

## Configuration

| File | What It Does | How It Helps |
|------|-------------|-------------|
| `settings.json.REFERENCE-ONLY` | Complete Claude Code settings with hooks, permissions, env vars, model config | Copy and customize — don't start from scratch |
| `templates/CLAUDE.md` | Identity template with routing table, role definition, essential standards | Your orchestration manifest — Claude knows who you are from session 1 |
| `QUICKSTART-PROMPT.md` | Paste into Claude Code for interactive guided setup | Claude builds your personalized config by asking you questions |

---

## Examples

| File | What It Shows | Why It Matters |
|------|-------------|---------------|
| `examples/compound-loop/README.md` | Full walkthrough: banned word mistake → memory → rule → hook → permanent prevention | Proves the compound effect is real, not theoretical |
| `examples/compound-loop/feedback-anti-slop-example.md` | What a real memory file looks like (with frontmatter) | Template for how corrections get stored |
| `examples/compound-loop/guardrail-example.py` | Simplified hook that catches banned words | Shows how hooks work in practice |

---

## The Compound Effect (Why All This Matters Together)

No single component is transformative on its own. The value is in how they interact:

```
Day 1:  You correct Claude → Memory file saved
Day 3:  Same mistake class → Rule prevents it automatically  
Day 7:  Rule might be forgotten in long sessions → Hook enforces mechanically
Day 14: Hook catches a pattern → Skill extracts it via /skillify
Day 30: Overnight crons feed new intel → Morning brief surfaces it
Day 60: Graph connects entities you didn't know were related → Better prep
```

Each layer reinforces the others. Memory feeds rules. Rules feed hooks. Hooks feed skills. Skills feed the graph. The graph feeds session-init. Session-init feeds the next conversation. The loop never stops.

**This is why starting matters more than perfecting.** A mediocre setup that runs for 60 days beats a perfect setup that runs for 1 day. Compound growth is the product.
