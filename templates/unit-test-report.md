# Apex 단위 테스트 리포트

## 입력 시나리오

- 세션 ID: `<sessionId>`
- 시나리오 JSON: `<scenarioInput.path>`
- 시나리오 승인 상태: `<scenarioInput.approvalStatus>`
- Org Alias: `<orgAlias>`
- 대상: `<target.component>`
- 진입점: `<target.entryPoint>`

## 생성 또는 수정한 테스트 파일

### 생성한 파일

- `<generatedFiles.path>`: `<generatedFiles.purpose>`

### 수정한 파일

- `<modifiedFiles.path>`: `<modifiedFiles.purpose>`

## 시나리오별 테스트 매핑

| 시나리오 | 상태 | 테스트 클래스 | 테스트 메서드 | 메모 |
| --- | --- | --- | --- | --- |
| `<scenarioId>` | `<status>` | `<testClass>` | `<testMethods>` | `<notes>` |

## 배포 검증 결과

- 시도 여부: `<deployment.attempted>`
- 상태: `<deployment.status>`
- 방식: `<deployment.method>`
- Job ID: `<deployment.jobId>`
- 상세:
  - `<deployment.details>`

## Apex 테스트 실행 결과

- 시도 여부: `<testRun.attempted>`
- 상태: `<testRun.status>`
- Test Run ID: `<testRun.testRunId>`
- 실행 테스트 수: `<testRun.testsRan>`
- 통과 수: `<testRun.passing>`
- 실패 수: `<testRun.failing>`
- 스킵 수: `<testRun.skipped>`
- 소요 시간 ms: `<testRun.durationMs>`

## Coverage 결과

| 이름 | 유형 | Coverage | 커버된 라인 | 미커버 라인 |
| --- | --- | --- | --- | --- |
| `<coverage.name>` | `<coverage.type>` | `<coverage.percentage>` | `<coverage.coveredLines>` | `<coverage.uncoveredLines>` |

## 실패 분석

| 클래스 | 메서드 | 분류 | 메시지 |
| --- | --- | --- | --- |
| `<failure.className>` | `<failure.methodName>` | `<failure.classification>` | `<failure.message>` |

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

- 실패가 없으면 E2E 검증 에이전트로 넘긴다.
- `fixRequests`가 있으면 개발 또는 수정 담당 에이전트가 먼저 처리한다.
