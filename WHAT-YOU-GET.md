# What You Get — Complete Inventory

Everything in this kit, what it does, why it's here, and how it helps you.

---

## Rules (13 Files) — Standards Claude Loads as Standing Instructions

Twelve of these load in every Claude Code session on their own, and `slds2-lwc-ui.md` only loads when you're working in LWC or Aura files, because its `paths:` frontmatter scopes it there.

| File | What It Does | Why It's Here |
|------|-------------|---------------|
| `communication.md` | Enforces SE voice: email under 200 words, Slack conventions, 70/30 customer-facing framing, banned email patterns, and anti-slop against the banned list in your CLAUDE.md | Every email, deck, and talk track sounds like YOU wrote it, not a chatbot |
| `security-governance.md` | CRUD/FLS and sharing enforcement, secrets handling, customer vs. internal content separation, permission sets over profiles, and a list of what never goes into git | Claude defaults to secure code and keeps sensitive data out of external prompts and commits |
| `architecture.md` | Decision framework, preferred patterns, anti-patterns, change design documentation | Architecture decisions are consistent and well-reasoned |
| `agent-script.md` | Agent Script file structure, the two-level action pattern, and syntax gotchas (written in May 2026 with `topic` blocks) | Syntax help; for the current `subagent` pattern, follow `BUILD-SPEC.md` and `reference-agent/` |
| `salesforce-instructions.md` | Senior SF SE persona, platform-first approach, inspect metadata before proposing | Claude acts like an experienced Salesforce Solutions Engineer |
| `salesforce-platform.md` | Bulk-safe Apex, thin triggers, one trigger per object, LWC best practices, named credentials | Production-quality Salesforce code that passes code review |
| `testing-quality.md` | Realistic test data, meaningful assertions (not just coverage), quality gate mindset | Tests that actually catch bugs, not just hit coverage numbers |
| `slds2-lwc-ui.md` | Base components first, SLDS 2 styling hooks with fallbacks, design tokens, no overrides of Salesforce-owned classes, accessibility; path-scoped to LWC and Aura files | Modern, compliant Lightning Web Components |
| `proof-before-claim.md` | "Done" needs a signal from the running system, not a commit or a clean compile | Stops confident "it's shipped" when nothing is behind it |
| `findings-are-perishable.md` | Re-check an old "X is broken" finding against the current artifact before acting on it | Stops you fixing things that were already fixed |
| `claims-faithful-to-source.md` | Re-read each claim against its source before an external doc ships; tag documented / inferred | Stops polished docs that quietly overstate the source |
| `refutation-needs-the-right-oracle.md` | Before calling something "fabricated," check the source where it would live if true | Stops confident wrong "that's made up" verdicts |
| `structural-voice.md` | Structure-level anti-AI rules: section symmetry, cadence, calibrated hedging | Content reads like a person wrote it, not just clean of banned words |

---

## Hooks (6 Wired by Setup + 2 Opt-In) — Scripts That Run Around Tool Calls

Hooks are scripts Claude Code runs before or after a tool call, so they don't depend on Claude remembering a rule late in a long session. They're written to catch a destructive command, a made-up product name, or a banned word at the moment it happens.

| File | When It Fires | What It Does | Why It's Here |
|------|--------------|-------------|---------------|
| `session-init.py` | Session start | Suggests wiki pages from your routing table by directory and branch, and shows the branch and uncommitted-change count | Every session starts with context — no "where was I?" |
| `guardrail.py` | Before Bash | Denies force-push to main, `--set-env-vars`, and `rm -rf` on `/`, `~`, or `.`, and asks you to confirm `git reset --hard` | Stops destructive mistakes at the point of action |
| `product-verification.py` | Before Edit/Write | Flags hallucinated Salesforce product names and writes a suggested correction | No more "Einstein Copilot" or "Agentforce Script" in customer content |
| `soql-schema-check.py` | Before Bash (`sf data query`) | Checks sObject and field names against the org's describe before the query runs, and denies the query with a "did you mean?" when a name doesn't exist | Catches bad SOQL before it fails in the org |
| `output-quality-gate.py` | After Write | Scans .md/.html/.txt files of 200+ words for 46 banned words and 20 banned phrases, and writes a warning with exact line numbers | Lightweight, node-free fallback for content quality |
| `voice-tell-gate.py` | After Write | Runs the full voice engine (score + your overlay + cadence) on written .md/.html/.txt files of 100+ words and writes a nudge; never blocks | Catches the rhythm tells a word list can't, and says so when it isn't calibrated to you yet |
| `gcp-tvm-guardrail.py` | Before Bash, **opt-in** | GCP security-compliance checks before deploys; hands Claude an advisory next to the command, never blocks | Only useful if you deploy to GCP, so setup leaves it off |

`graph-auto-index.py` (the knowledge-graph indexer below) ships in `hooks/scripts-optional/` and is also opt-in. It writes to its SQLite database directly and doesn't talk back to Claude.

**How the hooks talk back.** Every hook now uses the output format from the Claude Code hooks reference. A block is `hookSpecificOutput.permissionDecision` set to `"deny"`, or `"ask"` when you should confirm, and a nudge is `hookSpecificOutput.additionalContext`, which Claude reads next to the tool result. Earlier versions of this kit printed `{"result": "block"}`, a field Claude Code doesn't read, so the guardrail spotted a force-push and let it run anyway. I checked both versions with a headless `claude -p` run in a scratch repo with no remote: the old hook let `git push --force origin main` through, and the new one stopped it and quoted the reason back, even in bypass-permissions mode. If you installed before this fix, re-run `./setup.sh`. It upgrades any hook you haven't edited and leaves the ones you have alone.

---

## Skills (25 Commands) — Workflows Compressed into Single Commands

The time-saved column is my own estimate for each skill, and the range runs from about 15 minutes to 2 hours of manual work per run.

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

### Quality Assurance (5)

| Skill | What It Does | Time Saved |
|-------|-------------|-----------|
| `/validate` | Quality gate: 6 dimensions scored 1–10, SHIP / FIX FIRST / REWRITE verdict | Manual review → automated |
| `/review` | Sends a draft to a model from a different lab (OpenAI, Google, or xAI) for an adversarial read | A second opinion that doesn't share Claude's blind spots |
| `/voice-check` | Anti-slop scanner: full 50+ word banned list, replacements, pass/fail | Catches what you'd miss |
| `/voice-judge` | Gestalt read of a draft the way an expert reader would; can veto a clean score | Catches the tells regex can't |
| `/content-review` | 6-dimension universal reviewer with scoring rubric (accuracy, voice, specificity, customer-centricity, actionability, credibility) | Peer review → instant |

### Intelligence & Growth (5)

| Skill | What It Does | Time Saved |
|-------|-------------|-----------|
| `/morning-brief` | Daily context: overnight intel, git status, memory changes, suggested actions | 15 min orientation → instant |
| `/scan-intel` | Daily intelligence sweep: Exa web search, plus your X feed if you've set one up → categorized ADOPT NOW / EVALUATE / WATCH | 30 min research → 3 min |
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

### Code & Architecture (2)

| Skill | What It Does | Time Saved |
|-------|-------------|-----------|
| `/pr-review` | PR review against SF architecture and security standards | Manual review checklist → automated |
| `/gas-deploy` | Apps Script push + deploy + verify, so a `clasp push` never silently skips the web app | Prevents the push-only gotcha |

---

## Build on Agentforce (BUILD-SPEC.md + reference-agent/)

| Component | What It Does | How It Helps |
|-----------|-------------|-------------|
| `BUILD-SPEC.md` | 11-step build of a governed employee agent on GA primitives, a 14-row control map with each control's status as of release 264, from GA to beta to the one gap with no native equivalent yet, sources for every row, and a proof check on every build step | You can reproduce the Context Engineering series' Part 10 agent instead of just reading about it |
| `reference-agent/` | The working source: Agent Script agent, two Apex actions (`with sharing`, user mode, bulk-safe) with 9 tests, a permission set, seed data with a planted injection, and a held-out eval | Start from code that passed end to end on 2026-09-29, not from a blank org |

## Voice Engine and Review Scripts (tools/, harness-evolution/, scripts/)

| Component | What It Does | How It Helps |
|-----------|-------------|-------------|
| `tools/aiscore.mjs` + vendored detector | 0–100 AI score plus your personal overlay and cadence checks | The engine `voice-tell-gate.py` runs on |
| `tools/voice-setup.mjs` | The calibration fuse: labels every result "generic-only" until you've calibrated it to you | A clean score never gets mistaken for "sounds like me" |
| `harness-evolution/` | Held-out eval harness + a generic seed corpus you replace with your own writing | Prove a guard change is a real improvement |
| `tools/rag-quality/` + `tools/llm.mjs` | ECHO error attribution over Claude Code workflow traces (runs as-is), one query-rewrite tool that runs once `llm.mjs` points at your model, and three method skeletons you aim at your own corpus | Find which agent or step broke a multi-agent run |
| `scripts/llmgw-call.py`, `scripts/llmgw-review.py` + `scripts/review-prompts/` | Call any model on the Salesforce gateway; run the cross-vendor review behind `/review` with its adversarial or editorial prompt | Works with DevBar sign-in, no token copying |
| `scripts/check-cli.sh` | Detects installed CLIs and recommends what to add | Setup runs it first and stops if a required CLI is missing |

---

## Knowledge Graph (SQLite, Opt-In)

A local graph database that grows from your work. There's no external infrastructure, just Python and SQLite.

| Component | What It Does | How It Helps |
|-----------|-------------|-------------|
| `graph-auto-index.py` hook (opt-in) | Every Write/Edit indexes entities and computes relationships | Graph builds itself once you turn it on: copy `hooks/scripts-optional/graph-auto-index.py` to `~/.claude/hooks/scripts/` and register it as a PostToolUse hook on `Write\|Edit` |
| `graph-query` skill | Query relationships: "what relates to X?", "what mentions Y?" | Discover connections you didn't know existed |
| `wiki/entities/` | Company, product, concept pages indexed by the graph | Structured knowledge the graph can traverse |
| `wiki/people/` | Person pages with org trees and timelines | Relationship intelligence that compounds |

**How it compounds:** Write about a deal and the hook indexes the account, people, and products you mentioned. When you prep for that account later, `/graph-query` can pull up related wiki pages, other deals with the same people, and memory files you'd forgotten, as long as the indexer was on when you wrote them.

---

## Passive Intelligence (Crons, Overnight Growth)

Your knowledge base can grow overnight, but out of the box only one of these jobs is scheduled. The kit ships a single launchd plist, for `exa-scan.py` at 4:30 AM, so `manage.sh install` loads that one and warns about the hn and morning-digest plists it can't find. The other times in the table come from each script's own header, and to schedule one you copy the exa plist and change its `Label`, hour, and script path.

| Script | Schedule | What It Does | How It Helps |
|--------|----------|-------------|-------------|
| `exa-scan.py` | Daily 4:30 AM (plist included) | 5-query web intelligence (accounts, competitors, SF product, trends, Claude and MCP) | Morning brief has fresh web intel |
| `hn-scan.py` | Daily 4:45 AM (no plist yet) | 4-query Hacker News developer sentiment (free, no auth) | Know what developers are saying before customers mention it |
| `github-scan.py` | Daily 4:45 AM (no plist yet) | Trending AI repos + release monitoring on 10 agent frameworks and SDKs | What developers are actually adopting |
| `morning-digest.sh` | Daily 5:00 AM (no plist yet) | Synthesizes the day's raw intel files into `~/.claude/wiki/inbox.md` with `claude -p` | One place to check each morning |
| `memory-decay-check.sh` | Weekly, Sunday 6 AM (no plist yet) | Flags memory files unchanged >45 days | Catch stale knowledge before it misleads |
| `manage.sh` | Manual | Install / uninstall / status / test / logs for the launchd agents | One command to manage the whole system |

---

## Wiki Structure (7 Directories, Ready to Fill)

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
| `wiki/index.md` | Master catalog of all pages (Claude uses this to navigate); template in `templates/wiki/` | /ingest adds each new page; /wiki-lint checks it against the files |
| `wiki/inbox.md` | Staging area for overnight intel and captures | The morning digest prepends each day's intel |

---

## Configuration and Templates

| File | What It Does | How It Helps |
|------|-------------|-------------|
| `settings.json.REFERENCE-ONLY` | Annotated Claude Code settings with hooks, permissions, env vars, and model config; the `//` comments make it invalid JSON as written | Reference for merging hooks by hand; don't copy it over your `settings.json`, which holds your LLMGW auth key |
| `.mcp.json.REFERENCE-ONLY` | Annotated MCP server entries: the public Salesforce Docs MCP and a placeholder for the internal SE Grounding endpoint (the file's own header names `~/.claude/.mcp.json`, which isn't one of the locations the Claude Code MCP docs list) | Reference for `claude mcp add --transport http` (user scope lands in `~/.claude.json`) or for a project `.mcp.json` at a repo root, with the `//` comments stripped |
| `templates/CLAUDE.md` | Identity template with routing table, role definition, essential standards | Your orchestration manifest — Claude knows who you are from session 1 |
| `QUICKSTART-PROMPT.md` | Paste into Claude Code for interactive guided setup | Claude builds your personalized config by asking you 5 questions |
| `VOICE-ONBOARDING.md` | Six-step calibration of the voice guard to your own writing | Lifts the "generic-only" label once the guard knows your voice |
| `templates/apps-script/` + `docs/apps-script-setup.md` | Three starter Apps Script files (email merge, sheet data puller, slides from sheet) and the setup guide | Pairs with `/gas-deploy` |
| `templates/reports/` | HTML report templates for the morning brief, a session report, and system health | `/system-health` fills in its template |
| `docs/` | This inventory as HTML + PDF, and `SLIDES-FRAMEWORK.md`, a talk framework for presenting the kit | Hand-off material for your team |

---

## Examples

| File | What It Shows | Why It Matters |
|------|-------------|---------------|
| `examples/compound-loop/README.md` | Full walkthrough: banned word mistake → memory → rule → hook → permanent prevention | Proves the compound effect is real, not theoretical |
| `examples/compound-loop/feedback-anti-slop-example.md` | What a real memory file looks like (with frontmatter) | Template for how corrections get stored |
| `examples/compound-loop/guardrail-example.py` | Simplified hook that catches banned words | Shows how hooks work in practice |
| `examples/cross-vendor-loop/` | The real files from the Part 9 cross-vendor build loop: spec, starter tests, Sonnet's v1, the OpenAI and Google audits plus a note on Grok's timeout, the reconciliation that became the revised plan, four audit-derived failing tests, v1's red run, and the fixed v2 | 7 findings came down to 4 real bugs (two findings shared one root cause), 1 dismissal, and 1 spec-wording note, and each bug got a failing test before its fix. Both suites go green on plain Node, 5/5 and 4/4, and it all ran on my laptop with no Salesforce org involved |

---

## The Compound Effect (Why All This Matters Together)

Here's how the pieces feed each other over the first 60 days:

```
Day 1:  You correct Claude → Memory file saved
Day 3:  Same mistake class → Rule tells Claude to avoid it
Day 7:  Rule forgotten in long session → Hook checks mechanically
Day 14: Hook catches a pattern → /skillify extracts it into a new command
Day 30: Overnight crons feed intel → Morning brief surfaces it
Day 60: Graph (once you turn it on) connects entities → /graph-query surfaces related context
```

A correction you make on Day 1 only helps later if it lands somewhere Claude reads, which is why the timeline climbs from a memory file to a rule. The hook step is where it stops depending on Claude's memory, since a hook runs on every matching tool call whether the rule is still in context or not. The graph stays outside the chain until you turn it on, and after that it shows up through `/graph-query`.

**Starting matters more than perfecting.** A mediocre setup you use for 60 days will know more about your work than a perfect one you set up and leave alone, because what it knows comes from the corrections you store along the way. The kit hands you the memory, rules, and skills on the first day, and the loop only keeps going if you keep feeding it.
