# Obsidian-GitHub TIL 연동 프로젝트 연구 노트

- **문서 ID:** `P_PKM_Refinement_250706`
- **작성일:** `2025-07-09`
- **상태:** `계획 변경`

## 1. 프로젝트 개요

- **목표:** Obsidian에서 작성한 TIL 노트를 GitHub `kafkapple/TIL` 저장소와 자동으로 연동한다.
- **핵심 과제:**
    1.  Obsidian에서의 노트 작성 경험을 그대로 유지하며 GitHub 잔디 심기(commit)를 자동화한다.
    2.  여러 컴퓨터 환경의 서로 다른 경로 문제를 해결한다.
    3.  기존 `update_readme.py` 스크립트와의 통합.

---

## 2. 계획 A: Obsidian Git 플러그인 (실패)

가장 이상적인 자동화 방식인 `Obsidian Git` 플러그인 활용을 우선적으로 시도했으나, 플러그인이 Git 저장소를 인식하지 못하는 문제로 인해 실패했다.

### 문제 해결 과정 (Troubleshooting Log)

- **초기 증상:** 플러그인 설정에서 "Git is not ready" 메시지 발생.
- **시도 1: Git 사용자 정보 설정:** `git config user.name/email`을 저장소에 직접 설정했으나 변화 없음.
- **시도 2: Git 실행 파일 경로 명시:** `Custom git binary path`에 `which git`으로 찾은 `/usr/bin/git` 경로를 명시했으나 변화 없음.
- **시도 3: Git 저장소 경로 명시:** `Custom base path`에 TIL 저장소의 절대 경로(`/home/joon/Documents/Obsidian/10_Areas/TIL`)를 명시했으나 변화 없음.
- **시도 4: 디버깅 및 원인 분석:**
    - 개발자 도구 콘솔에서 `fatal: not a git repository` 오류 확인.
    - `ls -la` 명령어로 `.git` 폴더가 정상적으로 존재함을 확인.
- **시도 5: 설치 방식 확인 및 권한 부여:**
    - `snap`, `flatpak`, `apt` 명령어로 설치 방식을 확인, `.AppImage`로 추정. 샌드박스 가설 기각.
    - `git config --global --add safe.directory`로 저장소 경로를 안전한 디렉토리로 추가했으나 변화 없음.
- **시도 6: 문제 분리 테스트:**
    - 플러그인 문제를 분리하기 위해 깨끗한 `GitTest` 저장소를 새로 생성하여 연결 시도.
    - 여전히 동일한 "Git is not ready" 문제가 발생. **이를 통해 문제의 원인이 `TIL` 저장소가 아닌, 플러그인과 현재 시스템 환경의 호환성 문제임을 확인함.**
- **시도 7: 플러그인 설정 초기화:**
    - 플러그인의 설정 파일(`data.json`)을 직접 삭제하여 완전 초기화 후 최소 설정(base path)으로 재시도했으나 최종 실패.

### 결론

- 플러그인 자체의 버그, 혹은 현재 시스템의 특정 라이브러리/환경과의 호환성 충돌로 추정된다. 더 이상의 문제 해결은 시간 소모가 크다고 판단하여 **계획 A를 폐기하고 계획 B로 전환한다.**

---

## 3. 계획 B: 커스텀 동기화 스크립트

- **방향:** Obsidian 볼트의 TIL 노트를 로컬 GitHub 저장소 폴더로 복사하고, Git 작업을 자동화하는 Python 스크립트를 작성한다.

### 기본 로직
1.  **경로 설정:** 스크립트 또는 별도의 설정 파일에 Obsidian TIL 폴더(소스)와 GitHub TIL 폴더(타겟) 경로를 정의한다. (여러 컴퓨터 지원을 위해 복수 경로 정의)
2.  **파일 동기화:** 소스 폴더의 모든 `.md` 파일을 타겟 폴더로 복사/덮어쓰기 한다. (rsync 또는 shutil 활용)
3.  **README 업데이트:** 타겟 폴더로 이동하여 `update_readme.py` 스크립트를 실행한다.
4.  **Git 자동화:** `git add .`, `git commit -m "..."`, `git push` 명령을 순차적으로 실행한다.

### 다음 단계
- Python으로 동기화 스크립트(`sync_til.py`) 초안 작성 시작.
