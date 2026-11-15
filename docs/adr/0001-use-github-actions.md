
# ADR 0001: GitHub Actions를 활용한 자동화 도입

## Status
Accepted

## Context
프로젝트에서 DORA Metrics를 수집하고 관리하기 위해서는
GitHub 저장소의 변경 사항과 개발 활동을 지속적으로 확인해야 합니다.

수동으로 데이터를 수집하면 반복적인 작업이 발생하고
데이터 갱신이 늦어질 수 있다는 문제가 있습니다.

따라서 자동화된 작업 환경이 필요합니다.

## Decision
GitHub Actions를 사용하여 DORA Metrics 수집 및
관련 작업을 자동화하기로 결정했습니다.

GitHub Actions의 Workflow를 활용하여
프로젝트의 변경 사항에 따라 작업을 실행하고
수집 결과를 JSON 파일로 관리합니다.

## Alternatives

- 수동으로 데이터를 수집하고 관리하는 방법
- 별도의 외부 CI/CD 서비스를 사용하는 방법

## Consequences

### Positive
- 반복적인 데이터 수집 작업을 자동화할 수 있습니다.
- GitHub 저장소와 연동하기 쉽습니다.
- 작업 실행 내역을 확인할 수 있습니다.
- 별도의 서버 없이 자동화 환경을 구성할 수 있습니다.

### Negative
- Workflow YAML 파일을 작성하고 관리해야 합니다.
- GitHub Actions 사용량 제한을 고려해야 합니다.
- Workflow 오류 발생 시 별도의 수정 작업이 필요합니다.
