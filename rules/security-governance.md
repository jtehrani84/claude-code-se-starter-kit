# Security & Governance Rules

## Data Protection
- Never read or expose .env files, secrets, certificates, private keys, or auth tokens
- Never include customer names, account IDs, or deal values in prompts to external services
- Never upload sensitive content to public URLs, pastebins, or diagram renderers
- Mask sensitive values in examples

## Salesforce Security (for Apex/LWC work)
- Enforce record-level access with sharing-aware design
- Enforce object- and field-level access (CRUD/FLS) for queries and mutations
- Never recommend disabling sharing, CRUD/FLS checks, or platform protections as a shortcut
- Prefer named credentials and platform-native secret handling

## Content Governance
- Customer-facing content: no internal deal details, pricing, competitive positioning
- Internal content: can reference deals, pipeline, competitive intel
- Never mix audiences — double-check before sending
- PII handling: minimize, anonymize, never persist in plain text

## Permission Model
- Prefer permission sets over profiles
- Minimize privileged access
- Call out compliance-sensitive changes (PII, finance, healthcare)
- When asked to "just make it work," still preserve secure defaults

## What NOT to Commit to Git
- .env files or environment configs with secrets
- API keys, tokens, or credentials
- Customer-specific data (account IDs, deal values)
- Internal strategy documents
- Anything marked confidential or internal-only
