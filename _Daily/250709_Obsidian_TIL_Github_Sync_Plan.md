# Obsidian-GitHub TIL 연동 프로젝트 연구 노트

- **문서 ID:** `P_PKM_Refinement_250706`
- **작성일:** `2025-07-09`
- **상태:** `완료`

## 1. 프로젝트 개요
(중략)

## 2. 계획 A: Obsidian Git 플러그인 (실패)
(중략)

---

## 3. 계획 B: 커스텀 동기화 스크립트 (최종 채택)

- **방향:** Obsidian 볼트에서 조건에 맞는 TIL 노트를 지능적으로 탐색하여 GitHub 저장소로 동기화하고, Git 작업을 자동화하는 Python 스크립트(`sync_til.py`)를 작성한다.
- **최종 상태:** 모든 기능 구현 완료 및 `main` 브랜치에 통합 완료.

### 개발 및 문제 해결 과정

1.  **초안 작성:** Obsidian의 특정 폴더(`10_Areas/TIL`)를 GitHub 저장소 폴더로 복사하고 Git 작업을 수행하는 기본 스크립트 작성.
2.  **문제 발생 1: Git Push 실패**
    - **원인:** 로컬 브랜치에 업스트림(upstream)이 설정되지 않아 `git push`가 실패함.
    - **해결:** 현재 브랜치 이름을 동적으로 가져와 `git push --set-upstream origin <branch>`를 실행하도록 스크립트 수정.
3.  **요구사항 추가 1: 지능형 탐색**
    - **내용:** 특정 폴더가 아닌, Obsidian PKM 규칙에 따라 `10_Daily`, `30_Projects`, `40_Areas` 폴더 전체를 탐색하도록 기능 확장.
    - **해결:** `os.walk`를 사용하여 지정된 모든 폴더를 재귀적으로 탐색하는 로직 추가.
4.  **요구사항 추가 2: 누락된 노트 처리 및 Frontmatter 제거**
    - **내용:** 과거 노트 중 `tags: til`이 없어 동기화에서 누락되는 문제와, GitHub에 불필요한 Frontmatter가 포함되는 문제 해결 요청.
    - **해결 1 (태그 추가):** `add_til_tags.py` 유틸리티 스크립트를 별도로 작성. 파일명 규칙(`날짜_TIL_`)에 맞지만 태그가 없는 노트를 찾아 `tags: til`을 자동으로 추가해주는 기능을 구현하여 일괄 처리.
    - **해결 2 (Frontmatter 제거):** `sync_til.py`에 정규식을 활용하여, 파일 복사 시 Frontmatter 부분을 제거하고 순수 마크다운 본문만 저장하는 로직 추가.
5.  **문제 발생 2: Git Push 충돌**
    - **원인:** 로컬에서 작업하는 동안 원격 저장소의 `README.md`가 GitHub Actions에 의해 먼저 변경되어, `push`가 거부됨 (rejected).
    - **해결:** `git push` 이전에 `git pull --rebase` 명령을 추가하여, 원격의 변경사항을 먼저 로컬에 안전하게 통합한 후 푸시하도록 스크립트 최종 개선.

### 최종 스크립트 (`sync_til.py`) 핵심 기능

- **지능형 탐색:** `10_Daily`, `30_Projects`, `40_Areas` 폴더를 탐색하여 `tags: til`과 날짜 접두사 규칙을 만족하는 모든 노트를 식별.
- **증분 동기화:** 새롭거나 변경된 노트만 GitHub 저장소의 `_Daily` 폴더로 복사.
- **Frontmatter 제거:** 복사 시 노트 상단의 Frontmatter를 자동으로 제거하여 순수한 내용만 저장.
- **완전 자동화:** `update_readme.py` 실행, `git pull`, `add`, `commit`, `push`까지 모든 과��을 자동으로 처리.

