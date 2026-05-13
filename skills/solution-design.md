Design a complete solution architecture for a customer account. Produces branded internal strategy + customer-facing deliverables ready for team review and customer presentation.

**Input:** Account name (e.g., `/solution-design Acme Corp`)

---

## Phase 1: Channel Audit & CRM Context (parallel)

### 1A. Slack Channel Deep Read
- Read the full Slack channel (channel ID provided) — all messages, key threads
- Extract: key contacts, internal team, timeline of engagement, open action items, risks, customer's stated goals, technical environment, objections heard

### 1B. CRM Data Pull
- `crm_account_search` → find all account variants
- `crm_account_detail` → firmographics, owner, segment, tier
- `aip_account_activities` → recent engagement activity
- `crm_opportunity_history` → open opps, stages, amounts
- `crm_consumption_plans` → existing product usage

### 1C. Brand Resolution
- Scrape customer website using Firecrawl `branding` format
- Extract: primary color, secondary color, font family, logo URL, tone
- Store for deliverable generation

---

## Phase 2: Situation Synthesis

Produce a structured analysis (DO NOT output yet — hold for architecture questions):
- **What they think they want** (stated goals from Slack)
- **What they actually need** (gap between stated and real problem)
- **Their current tech stack** (what they have, what they're migrating to)
- **Key risks** (skeptics, bad taste, competing priorities, usage cliffs)
- **Internal team dynamics** (who drives, who blocks, who decides)
- **Open action items** (what's been promised but not delivered)

---

## Phase 3: Architecture Questions (2-3 key decisions)

Ask the user 2-3 architecture questions using AskUserQuestion. Typical questions:
- Do they need Agentforce reasoning, or just governed data access (Hosted MCP)?
- What's the right phase gate between quick-win and full investment?
- Is D360 relevant now or deferred (given "bad taste" or maturity level)?
- Is this a BYOLLM play (their models) or Agentforce-native?
- What's the NNAOV pathway — which SKUs unlock in Phase 2?

Base the questions on what was learned in Phase 1-2. Don't ask generic questions — ask the specific decision points that this deal requires.

---

## Phase 4: Build Deliverables

After user answers architecture questions, produce ALL of the following:

### 4A. Internal Strategy Document (`internal-strategy.md` + `.html`)
Contents:
- Situation (from channel audit)
- What they think they want vs what they actually need
- Recommendation: phased approach with timelines
- Success criteria gate between phases
- Competitive positioning table (their stack + our addition + why)
- Key objection handling (3-5 objections from Slack context)
- NNAOV pathway (Phase 1 → Phase 2 licensing)
- Team alignment needed (who does what)
- Risk statement

### 4B. Customer-Facing 1-Pager (`customer-facing-1pager.md` + `.html`)
Contents:
- Their goal (from their own words)
- The problem today (why current approach fails)
- Recommended architecture (visual diagram as styled divs)
- Phased delivery with timelines and "Your Effort" per phase
- What stays the same (don't fight their investments)
- What changes (before/after table)
- Cost model per phase
- Why this works (5 value props)
- Next steps (specific asks)

### 4C. Slides Content (`slides-content.json`)
- 9-slide structure matching the 1-pager content
- Structured JSON ready for Google Slides push

### HTML Styling Rules:
- Use customer's actual brand colors (from 1C)
- Light background, customer's primary color for headings/accents
- Open Sans or customer's actual font via Google Fonts
- Customer logo in header
- Internal version: same branding + "INTERNAL — DO NOT SHARE" banner
- Print stylesheet per `feedback-html-pdf-print-rules.md` memory (9.5pt, compressed spacing, forced page breaks at key sections)
- No blue unless it's the customer's brand color
- No AI-generated imagery — solid colors, typography, card layouts

### File Output Location:
All files go to: `TMT-CMRCL-MT/{account-name-kebab-case}/`

---

## Phase 5: Review & Iterate

Open both HTML files in browser for user review. User provides feedback on:
- Content accuracy
- Architecture positioning
- Timeline estimates
- Print/PDF quality

Iterate until user says "locked."

---

## Rules

- NEVER reference internal project names in customer-facing output
- NEVER use Salesforce blue unless it's genuinely the customer's brand color
- Timelines must reflect Claude build speed (2-3 weeks for Phase 1, not 4-6)
- Phase 2 is always gated on success metrics — never just "next quarter"
- Objection handling must use actual objections from the Slack channel, not generic ones
- "What stays the same" section is mandatory — always validate their existing investments
- Architecture diagrams use styled divs, not images
- All content passes VOICE_ANTI_SLOP — no banned words or structures
