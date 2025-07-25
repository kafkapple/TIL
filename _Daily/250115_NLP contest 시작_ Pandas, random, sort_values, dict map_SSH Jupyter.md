# Project
## NLP Contest: Dialogue summarization 시작
- 프로젝트 개요 정리
- baseline 코드 실행 및 모듈화
    - 기본 baseline
    - solar LLM
- submission
    - baseline BART
    - solar api
        - few-shot
- 교훈
    - LLM, prompt engineering 중요
# Study
### 1. **Pandas 관련 주요 코딩 패턴 요약**
### 1.1 **DataFrame 정렬 및 상위 n개 데이터 추출**
- `df.sort_values('column').head(n)` → 특정 컬럼 기준 정렬 후 상위 `n`개 데이터 선택.
### 1.2 **복사본 생성 경고(Warnings) 해결**
- **문제**: Pandas가 경고하는 "SettingWithCopyWarning".
- **해결**: 명시적으로 `.copy()` 사용.
    ```python
    python
    복사편집
    train_samples = df[df['column'] > 0].copy()
    train_samples.loc[idx, 'pred_summary'] = summary
    ```
### 1.3 **딕셔너리 평균값 계산**
- 각 키별 평균값 계산:
    ```python
    python
    복사편집
    averages = {key: sum(d[key] for d in data) / len(data) for key in data[0].keys()}
    ```
### 1.4 **딕셔너리 → DataFrame 변환**
- Key-Value 데이터를 DataFrame 컬럼으로 추가:
    ```python
    python
    복사편집
    for key, value in rouge_scores.items():
        df[key] = [value]
    ```
### 1.5 **키 매핑을 활용한 딕셔너리 변환**
- 키 매핑 딕셔너리로 기존 키를 새 키로 변환:
    ```python
    python
    복사편집
    transformed_dict = {key_map.get(k, k): v for k, v in original_dict.items()}
    ```
### 1.6 **재현 가능성을 위한 랜덤 시드 설정**
- NumPy 사용:
    ```python
    python
    복사편집
    np.random.seed(42)  # 원하는 시드 값 설정
    ```
### 1.7 **Few-shot Prompt 생성**
- 샘플 데이터 랜덤 선택:
    ```python
    python
    복사편집
    few_shot_samples = train_df.sample(1, random_state=42)
    sample_dialogue1 = few_shot_samples.iloc[0]['dialogue']
    ```
---
### 2. **SSH 서버와 VSCode 관련 문제**
### 2.1 **VSCode에서 SSH Remote와 Jupyter 사용 시 문제**
- **문제**: VSCode SSH Remote에서 Jupyter 환경을 실행할 때 올바른 환경이 선택되지 않음.
- **원인**: Python 인터프리터 경로가 일치하지 않거나 서버에 올바르게 설정되지 않음.
-