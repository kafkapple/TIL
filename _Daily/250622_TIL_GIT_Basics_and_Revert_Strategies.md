# 📄 GIT_Basics_and_Revert_Strategies

## ✨ 요약

Git의 기본적인 명령어와 커밋 취소 및 되돌리기 전략을 학습함.

## 📍 학습 내용

### 1. Git 기본 명령어

#### 1.1 초기 설정 및 원격 연결

- git init으로 로컬 저장소를 초기화함

- git remote add origin [URL]로 원격 저장소를 연결함

- git branch -M main으로 기본 브랜치 이름을 설정함
-> git switch -c main 더 선호

### 2. 커밋 되돌리기 전략

#### 2.1 로컬 커밋 취소

- git reset HEAD^ 또는 git reset --soft HEAD^로 마지막 커밋을 취소함

- git reset HEAD~n으로 여러 개의 로컬 커밋을 취소함

- git reset --hard는 되돌릴 수 없는 작업임을 인지함

#### 2.2 원격 커밋 취소 및 기록 유지

- git reset 후 git push -f로 원격 커밋을 강제로 취소함

- git revert HEAD를 사용하여 기록을 남기며 커밋을 취소함

### 3. 기타 유용한 도구

#### 3.1 스크립트 실행

- sh run.sh 명령어로 쉘 스크립트를 실행함을 확인함

#### 3.2 LLM 관련 도구

- litellm은 다양한 LLM API를 통합하는 도구임을 파악함

- promptfoo는 프롬프트 엔지니어링 테스트 도구임을 확인함