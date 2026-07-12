# E2E 검증 리포트

## 입력 시나리오

- 세션 ID: `<sessionId>`
- 시나리오 JSON: `<scenarioInput.path>`
- 시나리오 승인 상태: `<scenarioInput.approvalStatus>`
- Org Alias: `<orgAlias>`
- 대상: `<target.component>`
- 진입점: `<target.entryPoint>`

## 대상 Org 및 안전성 확인

- 확인 여부: `<orgSafety.checked>`
- 상태: `<orgSafety.status>`
- Org 유형: `<orgSafety.orgType>`
- Sandbox 여부: `<orgSafety.isSandbox>`
- 운영 org 차단 여부: `<orgSafety.productionBlocked>`
- 상세:
  - `<orgSafety.details>`

## 실행 범위

- 실행 모드: `<validationScope.executionMode>`
- 검증 채널: `<validationScope.channels>`
- 시나리오 ID: `<validationScope.scenarioIds>`

## 테스트 데이터 준비

| 시나리오 | Object | 목적 | Record ID | 외부 식별자 | 상태 | 정리 필요 |
| --- | --- | --- | --- | --- | --- | --- |
| `<scenarioId>` | `<object>` | `<purpose>` | `<recordIds>` | `<externalKeys>` | `<status>` | `<cleanupRequired>` |

## 검증 워크북

- Workbook: `<workbook.path>`
- 상태: `<workbook.status>`
- 비교 키: `<workbook.comparisonKeys>`
- CSV 대체 산출물 사용 여부: `<workbook.fallback.used>`
- CSV 대체 산출물 디렉터리: `<workbook.fallback.directory>`
- CSV 대체 사유: `<workbook.fallback.reason>`
- 메모:
  - `<workbook.notes>`

### Workbook 시트

| 시트 | 목적 | 상태 | 행 수 |
| --- | --- | --- | --- |
| `<sheet.name>` | `<sheet.purpose>` | `<sheet.status>` | `<sheet.rowCount>` |

### CSV 대체 파일

| 논리 시트 | 경로 | 상태 | 행 수 |
| --- | --- | --- | --- |
| `<logicalSheet>` | `<path>` | `<status>` | `<rowCount>` |

## 시나리오별 검증 결과

| 시나리오 | 상태 | 검증 유형 | 기대 결과 | 실제 결과 | 증거 | 실패 분류 |
| --- | --- | --- | --- | --- | --- | --- |
| `<scenarioId>` | `<status>` | `<validationType>` | `<expectedResult>` | `<actualResult>` | `<evidenceRefs>` | `<failureClassification>` |

## 시나리오 상세

### `<scenarioId>`

#### 실행 단계

- `<steps>`

#### 관찰 결과

- `<observations>`

#### 리스크

- `<risks>`

## 증거 목록

| ID | 유형 | 경로 또는 참조 | 설명 |
| --- | --- | --- | --- |
| `<id>` | `<type>` | `<pathOrRef>` | `<description>` |

## 정리 작업 결과

- 필요 여부: `<cleanup.required>`
- 상태: `<cleanup.status>`
- 정리 대상 목록: `<cleanup.manifestPath>`
- 메모:
  - `<cleanup.notes>`

### 정리 대상 Record

| Object | Record ID | 외부 식별자 | 작업 | 상태 |
| --- | --- | --- | --- | --- |
| `<object>` | `<recordId>` | `<externalKey>` | `<action>` | `<status>` |

## 실패 분석

- `<failure analysis>`

## 수정 요청 요약

| ID | 유형 | 대상 | 심각도 | 담당 | 상태 |
| --- | --- | --- | --- | --- | --- |
| `<fixRequest.id>` | `<fixRequest.type>` | `<fixRequest.target>` | `<fixRequest.severity>` | `<fixRequest.recommendedOwner>` | `<fixRequest.status>` |

## 남은 리스크와 다음 단계

### 가정

- `<assumptions>`

### 불확실한 점

- `<unknowns>`

### 다음 단계

- `<next steps>`
