---
paths:
  - "force-app/**/lwc/**/*.js"
  - "force-app/**/lwc/**/*.html"
  - "force-app/**/lwc/**/*.css"
  - "force-app/**/aura/**/*"
---

# SLDS 2 and UI Architecture Rules

## SLDS 2 principles
- Prefer Salesforce base components and SLDS patterns over custom-built controls.
- Do not depend on internal DOM structure or internal CSS classes of Lightning base components.
- Do not override SLDS/base component internals with brittle selectors.
- Use SLDS utility classes, component variants, and styling hooks.
- For SLDS 2-compatible customization, prefer global styling hooks and provide fallback values where needed.
- Keep UI accessible: semantic markup, labels, keyboard support, focus behavior, and sufficient contrast.
- Do not introduce custom styling that breaks theming, future upgrades, or dark-mode readiness.

## LWC styling rules
- Scope styles to the component.
- Use custom classes you own rather than targeting Salesforce-owned classes.
- Prefer design tokens / styling hooks / CSS custom properties when appropriate.
- Keep spacing, typography, and layout consistent with SLDS.
- Avoid pixel-perfect hacks unless absolutely unavoidable and documented.

## UX architecture
- Keep presentation and business logic separate.
- Components should have a single clear responsibility.
- Prefer composition over one huge all-knowing component.
- Build reusable child components when patterns repeat.
- Error states, loading states, and empty states must be handled intentionally.

## Output expectations
When producing LWC/UI changes:
- explain why the approach is SLDS 2 safe
- call out any styling hook usage
- call out accessibility considerations
- avoid unsupported CSS overrides
