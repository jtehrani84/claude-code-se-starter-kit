# Testing and Quality Rules

## Apex tests
- Write focused tests that validate behavior, not implementation trivia.
- Cover positive, negative, bulk, permission-sensitive, and edge scenarios where relevant.
- Use realistic test data.
- Avoid seeAllData=true unless there is no viable alternative and explain why.
- Assert meaningful outcomes, not just line coverage.
- Test for security-sensitive behavior where applicable.

## LWC tests
- Prefer Jest tests for component behavior when the repository supports it.
- Validate rendering, states, events, and user interactions.
- Mock Apex thoughtfully.
- Keep tests readable and resilient.

## Quality gate mindset
Before finalizing a solution, check:
- security
- limits
- test impact
- backward compatibility
- deployment dependencies
- admin operability
- user experience
