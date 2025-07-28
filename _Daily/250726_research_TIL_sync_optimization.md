# TIL 동기화 시스템 최적화 및 문제 해결

## 핵심 내용

### 문제 상황
- TIL 동기화 스크립트에서 코드 수정이 계속 초기화되는 문제 발생
- 히트맵의 월 라벨이 각 월의 시작점에 표시되어 가독성 저하
- README 파일명에서 TIL 접두사 제거 로직이 반복적으로 사라짐

### 근본 원인 분석
- `git_handler.py`의 `git_pull_rebase()` 함수에서 매번 `git reset --hard HEAD && git clean -fd` 실행
- 이로 인해 로컬 변경사항이 강제로 초기화되어 수정 내용이 유실됨
- sync.py 실행 시마다 원격 저장소 상태로 되돌아가는 구조적 문제

### 해결 방법
1. **직접 커밋 접근법**: sync 스크립트 실행 대신 직접 git commit으로 변경사항 보존
2. **월 라벨 중간 배치**: 각 월의 시작일이 아닌 중간 지점에 월 숫자 표시
3. **TIL 제거 로직**: 파일명에서 TIL_ 접두사를 제거하여 README 가독성 향상

### 기술적 구현
```python
# 월 라벨 중간 배치 로직
for month in range(1, 13):
    month_start = datetime(year, month, 1).date()
    month_end = datetime(year, 12, 31).date() if month == 12 else datetime(year, month + 1, 1).date() - timedelta(days=1)
    start_week = (month_start - start_of_first_week).days // 7
    end_week = (month_end - start_of_first_week).days // 7
    label_week = (start_week + end_week) // 2  # 중간점 계산
    if 0 <= label_week < total_weeks:
        month_labels[label_week] = f"{month:<2}"
```

## 교훈

### 시스템 설계 관점
- 자동화 스크립트에서 `git reset --hard`와 같은 파괴적 명령어는 신중히 사용해야 함
- 개발 중인 코드와 프로덕션 동기화 로직을 분리하는 것이 중요
- 로컬 변경사항 보존을 위한 안전장치가 필요

### 문제 해결 과정
- 반복적인 문제 발생 시 근본 원인을 찾는 것이 핵심
- 증상(코드 초기화)보다 원인(git reset 강제 실행)에 집중
- 임시 해결책보다 구조적 문제 해결이 장기적으로 효과적

### 코드 품질
- 사용자 경험을 고려한 시각적 개선(월 라벨 중간 배치)
- 가독성 향상을 위한 텍스트 정제(TIL 접두사 제거)
- 디버깅과 테스트를 통한 정확한 구현 검증

## Action Items

### 즉시 실행
- [x] 월 라벨 중간 배치 로직 구현 및 테스트 완료
- [x] TIL 제거 로직 추가 및 검증 완료
- [x] 변경사항 git 커밋으로 원격 저장소에 보존

### 향후 개선 사항
- [ ] sync.py 스크립트의 git reset 로직 재검토
- [ ] 개발 모드와 프로덕션 모드 분리 고려
- [ ] 변경사항 백업 메커니즘 추가 검토
- [ ] 히트맵 시각화 추가 개선 방안 검토

### 문서화
- [x] 문제 해결 과정을 연구 노트로 기록
- [ ] sync.py 스크립트 사용 가이드라인 업데이트
- [ ] git 워크플로우 모범 사례 정리

## 참고 자료
- TIL 저장소: `/home/joon/dev/TIL`
- 주요 파일: `src/readme_generator.py`, `src/git_handler.py`
- 커밋 해시: `0dc1510` (월 라벨 중간 배치 및 TIL 제거 로직 추가)