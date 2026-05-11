# Architecture & Quality Rules

## Decision Framework
Always choose the simplest approach that:
- Meets the requirement
- Scales reasonably
- Is understandable by the next person
- Is secure
- Is testable

## Preferred Patterns
- Thin triggers, reusable services, clear separation of concerns
- Encapsulate business logic in service/domain classes
- Centralize constants, error messages, and shared utility logic
- Keep orchestration separate from business rules
- Design for reuse across UI, automation, and integrations

## Anti-Patterns to Avoid
- Monolithic classes doing everything
- Duplicated logic everywhere
- Hardcoded IDs or environment assumptions
- UI components directly encoding business policy
- Deeply nested, hard-to-test logic
- Bypass flags without governance

## Change Design Output
For architecture-impacting work, always provide:
- Current-state issue
- Proposed design
- Alternatives considered
- Why this option was chosen
- Tradeoffs
- Deployment considerations

## Quality Gate
Before finalizing any solution, check:
- Security implications
- Governor limits (for Salesforce)
- Test coverage
- Backward compatibility
- Deployment dependencies
- User experience impact
