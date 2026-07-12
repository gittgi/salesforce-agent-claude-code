# MCP / CLI First Runbook

This runbook describes how Claude Code should operate the Salesforce Test Agent MVP without relying on the Python executor as the primary runtime.

## Output Language

User-facing artifacts must be written in Korean by default:

- Markdown reports, approval prompts, summaries, workbook/CSV display labels, and human-readable JSON description strings.
- Keep schema keys, file names, paths, Apex/API identifiers, SOQL, CLI commands, metadata names, record IDs, and schema enum values in their original English/API form.
- Do not use default English report headings such as "Report", "Summary", "Evidence", "Status", "Next Actions", or "Cleanup" in user-facing Markdown unless they are part of an API value or file path.

## 1. Preflight

Use Salesforce DX MCP first:

```text
mcp__salesforce_dx.list_all_orgs(directory=<workspace>)
```

Then verify the target org with read-only checks:

```bash
sf org display --target-org <alias> --json
sf data query --target-org <alias> --query "SELECT Id, Name, OrganizationType, IsSandbox, InstanceName FROM Organization" --json
```

Block Production. Continue only for non-production orgs.

## 2. Create Session Folder

Use a timestamped folder:

```text
test-results/YYYYMMDD-HHMMSS-<component>/
```

Create these files as the workflow progresses:

- `scenario.json`
- `scenario-review.md`
- `report.md`
- `validation.xlsx`
- `fix-requests.json`
- `cleanup-manifest.json`

## 3. Context Analysis

Prefer MCP metadata retrieval when local files are missing:

```text
mcp__salesforce_dx.retrieve_metadata(...)
```

For quick read-only Apex inspection, use Tooling API through `sf` CLI:

```bash
sf data query --use-tooling-api --target-org <alias> \
  --query "SELECT Id, Name, Body, ApiVersion FROM ApexClass WHERE Name = '<ClassName>' LIMIT 1" \
  --json
```

Trigger inspection:

```bash
sf data query --use-tooling-api --target-org <alias> \
  --query "SELECT Id, Name, Body, TableEnumOrId FROM ApexTrigger WHERE Name = '<TriggerName>' LIMIT 1" \
  --json
```

Generate Given / When / Then scenarios manually as Claude Code, following official Salesforce testing guidance.

## 4. Scenario Review Gate

Write `scenario-review.md` and `scenario.json`.

Ask the user for approval before:

- generating or modifying Apex test classes
- deploying metadata
- running Apex tests
- mutating org data

## 5. Apex Test Class Generation

Use official Apex test guidance:

- one behavior per method
- `@IsTest`
- `SeeAllData=false` by default
- `Test.startTest()` / `Test.stopTest()`
- meaningful `Assert.*` assertions
- bulk path with 251 records when relevant

Write both files:

```text
force-app/main/default/classes/<ClassName>Test.cls
force-app/main/default/classes/<ClassName>Test.cls-meta.xml
```

Do this only after the test-code approval gate.

## 6. Deploy Test Metadata

Validate first:

```bash
sf project deploy start \
  --dry-run \
  --source-dir force-app/main/default/classes \
  --target-org <alias> \
  --wait 10 \
  --json
```

Deploy only after explicit confirmation:

```bash
sf project deploy start \
  --source-dir force-app/main/default/classes \
  --target-org <alias> \
  --wait 10 \
  --json
```

## 7. Run Apex Tests

Prefer MCP when available:

```text
mcp__salesforce_dx.run_apex_test(
  directory=<workspace>,
  usernameOrAlias=<alias>,
  testLevel="RunSpecifiedTests",
  classNames=["<ClassName>Test"],
  codeCoverage=true
)
```

CLI fallback:

```bash
sf apex run test \
  --target-org <alias> \
  --test-level RunSpecifiedTests \
  --class-names <ClassName>Test \
  --result-format json \
  --code-coverage \
  --wait 10 \
  --json
```

Write results to `report.md` and `validation.xlsx`, using Korean for all user-facing report text.

## 8. Dev Validation

Run only after dev-validation approval.

For DML scenarios, use `sf data`:

```bash
sf data create record --target-org <alias> --sobject Account --values "Name='TEST_AGENT_TC001_Account'" --json
sf data update record --target-org <alias> --sobject Account --record-id <id> --values "Description='...'" --json
sf data delete record --target-org <alias> --sobject Account --record-id <id> --json
```

For simple service calls, use Anonymous Apex:

```bash
sf apex run --target-org <alias> --file anonymous.apex --json
```

Record every created record in `cleanup-manifest.json`.

## 9. Cleanup

Delete records listed in `cleanup-manifest.json`.

After cleanup, verify records no longer exist with read-only SOQL.

## 10. Failure Handling

When a scenario fails:

1. Capture expected vs actual.
2. Capture evidence.
3. Identify likely cause.
4. Create `fix-requests.json`.
5. Do not modify production Apex code.
