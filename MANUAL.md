# TIL Project Manual

## 1. 프로젝트 목적

이 프로젝트는 [Obsidian](https://obsidian.md/)에서 작성한 TIL(Today I Learned) 노트를 GitHub 저장소로 자동으로 동기화하고, 보기 좋은 대시보드(`README.md`)를 생성하기 위해 만들어졌습니다.

주요 기능은 다음과 같습니다:
- Obsidian의 TIL 노트를 GitHub 저장소로 복사
- 노트 내용에서 불필요한 메타데이터(Area, Dataview 등) 자동 제거
- `README.md`에 GitHub 잔디와 같은 히트맵(Heatmap) 및 전체 목차 자동 생성
- Git `pull`, `add`, `commit`, `push` 과정을 한 번에 처리

---

## 2. 폴더 구조

프로젝트는 다음과 같은 구조로 이루어져 있습니다.

```
TIL/
├── _Daily/           # 정리된 TIL 노트가 저장되는 곳
├── src/              # 핵심 로직을 담은 소스 코드 폴더
│   ├── file_handler.py       # 파일 탐색, 정리, 복사
│   ├── git_handler.py        # Git 관련 명령어 처리
│   └── readme_generator.py   # README.md 생성
├── utils/            # 가끔 사용하는 유틸리티 스크립트 폴더
│   └── cleanup_til_notes.py  # 기존 모든 노트를 강제로 정리
├── sync.py           # ✨ 메인 실행 스크립트
├── MANUAL.md         # (현재 파일) 사용 설명서
└── README.md         # 자동 생성되는 대시보드
```

---

## 3. 핵심 사용법

Obsidian에서 TIL 노트 작성을 마친 후, 터미널에서 아래의 명령어 하나만 실행하면 모든 동기화 작업이 자동으로 처리됩니다.

```bash
python3 sync.py
```

이 명령어는 다음 작업을 순서대로 수행합니다:
1.  원격 저장소의 변경사항을 먼저 가져옵니다 (`git pull --rebase`).
2.  Obsidian 볼트에서 새로운 TIL 노트를 찾아 `_Daily` 폴더로 복사하고 정리합니다.
3.  `README.md` 파일의 히트맵과 목차를 최신 상태로 업데이트합니다.
4.  모든 변경사항을 원격 저장소로 푸시합니다 (`git push`).

---

## 4. 유지보수 및 문제 해결

### 기존 노트 전체 강제 정리

만약 스크립트 로직 변경 등으로 인해 `_Daily` 폴더에 있는 모든 노트의 내용을 한꺼번에 정리하고 싶을 경우, 아래의 유틸리티 스크립트를 사용하세요.

**주의: 이 스크립트는 폴더 내의 모든 `.md` 파일을 직접 수정합니다.**

```bash
python3 utils/cleanup_til_notes.py --force
```
