# E2E Validation Report

## 입력 시나리오

- 세션 ID: `<sessionId>`
- Scenario JSON: `<scenarioInput.path>`
- Scenario approval: `<scenarioInput.approvalStatus>`
- Org Alias: `<orgAlias>`
- 대상: `<target.component>`
- Entry Point: `<target.entryPoint>`

## 대상 Org 및 안전성 확인

- Checked: `<orgSafety.checked>`
- Status: `<orgSafety.status>`
- Org Type: `<orgSafety.orgType>`
- Is Sandbox: `<orgSafety.isSandbox>`
- Production Blocked: `<orgSafety.productionBlocked>`
- Details:
  - `<orgSafety.details>`

## 실행 범위

- Execution Mode: `<validationScope.executionMode>`
- Channels: `<validationScope.channels>`
- Scenario IDs: `<validationScope.scenarioIds>`

## 테스트 데이터 준비

| Scenario | Object | Purpose | Record IDs | External Keys | Status | Cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| `<scenarioId>` | `<object>` | `<purpose>` | `<recordIds>` | `<externalKeys>` | `<status>` | `<cleanupRequired>` |

## 검증 워크북

- Workbook: `<workbook.path>`
- Status: `<workbook.status>`
- Comparison Keys: `<workbook.comparisonKeys>`
- Fallback Used: `<workbook.fallback.used>`
- Fallback Directory: `<workbook.fallback.directory>`
- Fallback Reason: `<workbook.fallback.reason>`
- Notes:
  - `<workbook.notes>`

### Workbook Sheets

| Sheet | Purpose | Status | Rows |
| --- | --- | --- | --- |
| `<sheet.name>` | `<sheet.purpose>` | `<sheet.status>` | `<sheet.rowCount>` |

### Workbook Fallback Files

| Logical Sheet | Path | Status | Rows |
| --- | --- | --- | --- |
| `<logicalSheet>` | `<path>` | `<status>` | `<rowCount>` |

## 시나리오별 검증 결과

| Scenario | Status | Type | Expected | Actual | Evidence | Failure Classification |
| --- | --- | --- | --- | --- | --- | --- |
| `<scenarioId>` | `<status>` | `<validationType>` | `<expectedResult>` | `<actualResult>` | `<evidenceRefs>` | `<failureClassification>` |

## 시나리오 상세

### `<scenarioId>`

#### Steps

- `<steps>`

#### Observations

- `<observations>`

#### Risks

- `<risks>`

## 증거 목록

| ID | Type | Path or Ref | Description |
| --- | --- | --- | --- |
| `<id>` | `<type>` | `<pathOrRef>` | `<description>` |

## Cleanup 결과

- Required: `<cleanup.required>`
- Status: `<cleanup.status>`
- Manifest: `<cleanup.manifestPath>`
- Notes:
  - `<cleanup.notes>`

### Cleanup Records

| Object | Record ID | External Key | Action | Status |
| --- | --- | --- | --- | --- |
| `<object>` | `<recordId>` | `<externalKey>` | `<action>` | `<status>` |

## 실패 분석

- `<failure analysis>`

## Fix Request 요약

| ID | Type | Target | Severity | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| `<fixRequest.id>` | `<fixRequest.type>` | `<fixRequest.target>` | `<fixRequest.severity>` | `<fixRequest.recommendedOwner>` | `<fixRequest.status>` |

## 남은 리스크와 다음 단계

### 가정

- `<assumptions>`

### 불확실한 점

- `<unknowns>`

### 다음 단계

- `<next steps>`
