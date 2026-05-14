Review a pull request against Salesforce architecture, security, and quality standards. Takes a PR number or URL as argument.

## Step 1: Get PR Context

```bash
gh pr view [PR_NUMBER] --json title,body,files,additions,deletions,changedFiles
gh pr diff [PR_NUMBER]
```

## Step 2: Review Checklist

### Security Review (CRITICAL — every PR)

For each Apex class/trigger changed:
- [ ] **Sharing model:** Is the class `with sharing`? If `without sharing`, is there documented justification?
- [ ] **CRUD/FLS enforcement:** Are queries using `WITH USER_MODE` or `stripInaccessible`? Are DML operations checking permissions?
- [ ] **Injection risks:** Any dynamic SOQL/SOSL? Is input sanitized? Are bind variables used?
- [ ] **Governor limits:** Any SOQL/DML inside loops? Are collections and maps used for efficiency?
- [ ] **Data exposure:** Are sensitive fields exposed to UI/API without access validation?
- [ ] **Secrets:** Any hardcoded IDs, URLs, API keys, credentials, tokens?
- [ ] **Input validation:** Is user input validated at system boundaries?

### Architecture Review

- [ ] **Thin triggers:** Is logic in handler/service/domain classes, not in the trigger itself?
- [ ] **One trigger per object:** No second trigger introduced on an existing object?
- [ ] **Service layer:** Business logic in reusable service classes?
- [ ] **No SOQL in loops:** All queries bulkified?
- [ ] **No DML in loops:** All DML bulkified?
- [ ] **Recursion guards:** Explicit, well-designed recursion prevention?
- [ ] **Error handling:** Meaningful exceptions, not swallowed errors?
- [ ] **Naming conventions:** Consistent with existing codebase patterns?

### LWC Review (if applicable)

- [ ] **SLDS 2 compliance:** Using base components and styling hooks?
- [ ] **Reactive state:** Simple, focused components?
- [ ] **Wire vs imperative:** Appropriate choice for data access?
- [ ] **Error handling:** User-facing error messages (toast notifications)?
- [ ] **Accessibility:** ARIA labels, keyboard navigation?

### Test Review

- [ ] **Test exists:** Every changed class has corresponding test coverage?
- [ ] **Bulk tests:** Testing with 200+ records?
- [ ] **Negative tests:** Testing error conditions and edge cases?
- [ ] **No seeAllData:** Tests use test data, not org data?
- [ ] **Meaningful assertions:** Asserting behavior, not just coverage?
- [ ] **Permission tests:** Testing with different permission sets?

### Deployment Review

- [ ] **Backward compatible:** No breaking changes to existing APIs or metadata?
- [ ] **Dependencies:** Are all referenced metadata included in the PR?
- [ ] **Profiles/PermSets:** Any permission changes documented?
- [ ] **Blast radius:** How many users/processes does this change affect?

## Step 3: Output Format

```
## PR Review — #[NUMBER]: [Title]

### Verdict: APPROVE / REQUEST CHANGES / NEEDS DISCUSSION

### Score: X/10

### Security Findings
| Severity | File | Issue | Fix |
|----------|------|-------|-----|
| CRITICAL | ... | ... | ... |
| HIGH | ... | ... | ... |

### Architecture Findings
...

### Test Coverage
- Lines added: X
- Lines with test coverage: X
- Coverage gap: [files without tests]

### Recommendations
1. [Most important fix]
2. [Second]
3. [Third]

### What's Good
- [Positive callout 1]
- [Positive callout 2]
```
