# Entity Pages — People Knowledge Base

## What These Are

Entity pages are structured profiles for the people you work with. They give Claude persistent memory about individuals so you don't re-explain relationships, preferences, and context every session.

Over time, these compound: meeting notes get appended, decision styles get refined, relationship maps fill in. After 30 days, Claude knows your key stakeholders as well as you do.

## Two Templates

**Internal** (`_template-internal.md`): Colleagues, managers, peers, cross-functional partners.
Focus: working style, current focus, how to collaborate effectively.

**External** (`_template-external.md`): Customers, prospects, partners, analysts.
Focus: decision style, stated priorities, relationship map, engagement history.

## How to Seed Them

### From Slack profiles (fastest)
Tell Claude: "Create an entity page for [Name] — they're [role] at [company]."
Claude will ask a few questions and generate the page.

### From meeting notes
After a meeting: "Add what we learned about [Name] to their entity page."
Claude appends to the engagement timeline.

### From CRM data
If you have Salesforce access: "Pull contact info for [Name] at [Company] and create their entity page."
Claude uses CRM data as the foundation.

### From LinkedIn
Share a LinkedIn URL: "Create an external entity page from this profile."
Claude extracts role, company, career trajectory.

## How They Compound

**Week 1:** Basic profile. Name, title, one or two notes.

**Week 4:** Decision style documented from 2-3 interactions. Relationship map has key players. You know their communication preference.

**Week 8:** Engagement timeline shows patterns. You can predict their objections. Claude references their stated priorities automatically in prep docs.

**Week 12:** The profile is richer than your CRM record. Meeting prep references their specific concerns by name. Email drafts use their language patterns.

## File Naming Convention

```
wiki/people/
  firstname-lastname.md          # Standard format
  firstname-lastname-company.md  # If name collision
```

Examples:
- `sarah-chen.md` (internal colleague)
- `david-park-acme.md` (external contact at Acme Corp)

## Privacy

These files are local to your machine. They are NOT committed to shared repositories unless you explicitly choose to. The `.gitignore` in setup excludes `wiki/people/` from public repos by default.

For team-shared entity pages (e.g., key accounts), use a private team repo.
