# Salesforce Platform Development Rules

## General development approach
- Prefer declarative solutions first:
  - validation rules
  - Flow
  - approval/process capabilities
  - standard objects/features
- Use Apex only when declarative tools are insufficient for scale, complexity, transaction control, reuse, or external integration.
- Use Lightning Web Components for UI work unless there is a compelling reason not to.
- Avoid Aura for net-new work except where platform constraints require it.
- Use standard base components before creating custom UI primitives.

## Apex rules
- All Apex must be bulk-safe.
- Never perform SOQL or DML inside loops unless there is a very strong, documented reason.
- Use collections and maps to reduce query and CPU overhead.
- Keep triggers thin. Put logic in handler/service/domain classes.
- One trigger per object.
- Triggers should orchestrate only; business logic belongs in reusable classes.
- Avoid recursion with explicit, well-designed guards.
- Handle partial success deliberately where relevant.
- Use meaningful exception handling. Do not swallow exceptions.
- Prefer platform events, queueables, batch, scheduled jobs, or async patterns for long-running work.
- Be conscious of transaction boundaries and mixed DML.

## LWC rules
- Prefer reactive, simple state.
- Keep components focused and small.
- Move business logic to Apex or shared JS utilities when appropriate.
- Use @wire when reactive data access is appropriate; use imperative Apex when control is needed.
- Cache when safe and appropriate.
- Avoid unnecessary server round trips.
- Respect Lightning Locker / Lightning Web Security constraints.

## Data and integration
- Prefer named credentials and external credentials for callouts and integrations.
- Never embed secrets in source.
- Document integration contracts, retries, timeouts, and failure modes.
- Be explicit about idempotency and duplicate handling.

## Metadata and packaging
- Keep source organized and deployment-friendly.
- Do not rename metadata casually.
- Avoid changes that create unnecessary deployment dependencies.
- Call out whether a change affects profiles, permission sets, record types, layouts, flows, or API integrations.
