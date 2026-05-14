# Entity Pages — Companies, Products, Concepts

This directory holds structured pages for non-person entities that you interact with repeatedly. The knowledge graph indexes these automatically.

## What Goes Here

- **Companies** — accounts you work with, competitors, partners
- **Products** — Salesforce products, competitor products, customer technology
- **Concepts** — patterns, frameworks, methodologies you reference across sessions

## Template

```markdown
# [Entity Name]

## Type
Company | Product | Concept | Competitor

## Summary
[One paragraph: what this is and why it matters to your work]

## Key Facts
- [Fact 1 with source]
- [Fact 2 with source]
- [Fact 3 with source]

## Relationships
- [Related to: person, company, deal, concept]

## Notes
[Anything that doesn't fit above — gotchas, open questions, things to verify]

---

## Timeline
<!-- Append interactions, changes, news. Newest at top. -->
```

## How It Grows

1. **Manually** — Create a page when you encounter an entity you'll reference again
2. **From /account-prep** — Account research can auto-create a company page
3. **From /post-meeting** — Meeting outcomes can reference/create entity pages
4. **From /ingest** — Processing a new source can extract entities into pages

## Naming Convention

Use lowercase with hyphens: `acme-corp.md`, `agentforce.md`, `data-cloud.md`

## How the Graph Uses These

The `graph-auto-index.py` hook scans all files for mentions of entity names. When your memory file mentions "Agentforce" and you have `wiki/entities/agentforce.md`, the graph creates a REFERENCES edge. Over time, this reveals which topics, people, and files cluster together — surfacing context you didn't know was connected.
