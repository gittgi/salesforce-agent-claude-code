# 테스트 시나리오 리뷰

## 분석 대상

- 세션 ID: `<sessionId>`
- Org Alias: `<orgAlias>`
- 대상 유형: `<target.type>`
- 대상 컴포넌트: `<target.component>`
- 진입점: `<target.entryPoint>`
- 소스 참조: `<target.sourceRef>`

## 변경 또는 명시 코드 요약

`<analysisSummary.targetResolution>`

## 코드가 수행하는 역할

### 확인된 동작

- `<confirmedBehavior>`

### 추론한 동작

- `<inferredBehavior>`

## 주요 의존성

| 유형 | 이름 | 이유 |
| --- | --- | --- |
| `<dependency.type>` | `<dependency.name>` | `<dependency.reason>` |

## 테스트 시나리오 목록

| ID | 우선순위 | 유형 | 제목 |
| --- | --- | --- | --- |
| `<scenarioId>` | `<priority>` | `<scenarioType>` | `<title>` |

## 시나리오 상세

### `<scenarioId>` - `<title>`

- 우선순위: `<priority>`
- 유형: `<scenarioType>`
- 대상 파일: `<sourceTarget.path>`
- 비즈니스 동작: `<businessBehavior>`

#### Given / 전제

`<given>`

#### When / 실행

`<when>`

#### Then / 결과

`<then>`

#### 기대 결과

`<expectedResult>`

#### 필요한 테스트 데이터

| Object | 목적 | 필드 | 건수 |
| --- | --- | --- | --- |
| `<object>` | `<purpose>` | `<fields>` | `<recordCount>` |

#### 단위 테스트 관점 메모

- 준비: `<unitTestNotes.setupGuidance>`
- 검증: `<unitTestNotes.assertions>`
- `Test.startTest()` / `Test.stopTest()` 필요: `<unitTestNotes.requiresStartStopTest>`
- 대량 처리 coverage 필요: `<unitTestNotes.requiresBulkCoverage>`
- Mocking 필요사항: `<unitTestNotes.mockingNeeds>`
- 특이사항: `<unitTestNotes.specialConsiderations>`

#### E2E 검증 관점 메모

- 준비: `<e2eValidationNotes.setupGuidance>`
- 실행 단계: `<e2eValidationNotes.executionSteps>`
- 관찰 포인트: `<e2eValidationNotes.observations>`
- Org 데이터 변경 필요: `<e2eValidationNotes.requiresOrgDataMutation>`
- 사용자 승인 필요: `<e2eValidationNotes.requiresUserApproval>`
- 정리 작업: `<e2eValidationNotes.cleanupSteps>`
- 특이사항: `<e2eValidationNotes.specialConsiderations>`

#### 리스크

- `<risks>`

#### 가정

- `<assumptions>`

#### 불확실한 점

- `<unknowns>`

#### 정리 작업 고려사항

- `<cleanupConsiderations>`

## 전체 가정 및 불확실한 점

### 가정

- `<assumptions>`

### 불확실한 점

- `<unknowns>`

### 후속 질문

- `<followUpQuestions>`

## 사용자 승인 필요 여부

- 승인 단계: `<approval.stage>`
- 승인 상태: `<approval.status>`
- 승인 필요: `<approval.required>`
