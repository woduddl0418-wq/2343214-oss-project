# oss-project
# 대학생 과제 관리 웹사이트

## 1. 프로젝트의 목적
대학생들이 여러 과목의 과제와 마감일을 한곳에서 관리하고, 과제 진행 상황을 쉽게 파악할 수 있도록 돕는 웹서비스를 개발한다.

## 2. 문제 정의
과목마다 과제와 제출 기한이 다르기 때문에 마감일을 놓치거나 진행 상황을 체계적으로 관리하기 어렵다. StudyFlow는 과제를 통합 관리하여 이러한 불편을 줄이는 것을 목표로 한다.

## 3. 핵심 기능
1. 과제 등록, 조회, 수정 및 삭제
2. 과목별 과제 목록과 마감일 관리
3. 과제 상태 변경 및 전체 완료율 표시

## 4. 기술 스택
- 프론트엔드: HTML, CSS, JavaScript
- 백엔드: Java, Spring Boot
- 데이터베이스: MySQL (기본 기능 구현 후 연동)
- 협업 및 형상 관리: Git, GitHub
- 자동화: GitHub Actions

## 5. 개발 계획
- 1~4주차: 개발 환경 구축, 요구사항 분석 및 화면 설계
- 5~8주차: 과제 관리 기능과 백엔드 구현
- 9~12주차: 데이터베이스 연동 및 테스트
- 13~16주차: 자동화, 사용성 개선, 배포 및 문서화

## 6. 기대 효과
과제 누락을 줄이고 학업 일정을 효율적으로 관리할 수 있고, GitHub 기반 개발 과정과 자동화 도구의 활용 경험도 쌓을 수 있다.



# DORA Metrics Collection Automation

## 1. 프로젝트 개요
GitHub Actions를 이용하여 DORA 4대 지표를 자동으로 수집하고 JSON 파일로 저장한다.

## 2. DORA 4대 지표
- **Lead Time for Changes:** 코드 변경부터 배포까지 걸리는 시간
- **Deployment Frequency:** 일정 기간 동안의 배포 빈도
- **MTTR:** 장애 발생 후 복구까지 걸리는 시간
- **Change Failure Rate:** 배포 중 실패한 변경의 비율

## 3. 파일 구조
- `.github/workflows/dora-metrics.yml`: GitHub Actions 자동 실행 설정
- `metrics/events.csv`: 이벤트 데이터
- `metrics/dora-metrics.json`: DORA 지표 계산 결과
- `scripts/collect_metrics.py`: 지표 계산 스크립트

## 4. 실행 방법
GitHub Actions에서 DORA Metrics Collection 워크플로를 실행한다. 실행 결과는 `metrics/dora-metrics.json`에 저장된다.

## 5. 결과 확인
GitHub Actions 실행 기록에서 작업 성공 여부를 확인하고, 생성된 JSON 파일에서 DORA 지표를 확인한다.
