### 데이터셋 분할 방법 요약 (2024-11-06)
---
## 1. Holdout
- **방법**:
    - 데이터를 일정 비율로 분리(예: 8:2).
    - **시계열 데이터**에서 자주 사용.
- **유형**:
    - 랜덤 분할: 데이터에서 무작위로 학습/검증 세트 생성.
    - 최근 20%를 검증 세트로 사용: 미래 예측 목적.
- **특징**:
    - 간단하고 직관적이지만, 검증 신뢰도가 낮을 수 있음.
---
## 2. K-Fold 교차 검증
- **방법**:
    - 데이터를 k개의 폴드로 나눔. 
    - k−1 개의 폴드로 학습하고, 1개의 폴드로 검증을 반복 (k번).
- **장점**:
    - 전체 데이터를 학습에 활용 가능.
    - 검증 신뢰도 향상.
    - 앙상블 효과 제공.
---
## 3. Stratified K-Fold
- **특징**:
    - K-Fold와 동일한 구조.
    - **차이점**:
        - 각 폴드에서 타겟 변수(y)의 클래스 비율을 유지.
            yy
        - 클래스 불균형 문제를 해결할 수 있음.
---
## 4. Group K-Fold
- **특징**:
    - 폴드 내 데이터가 특정 그룹에 따라 분리되도록 설정.
    - 각 폴드에 동일 그룹의 데이터가 겹치지 않도록 처리.
- **사용 사례**:
    - 동일 그룹 내 샘플이 서로 유사하거나 의존적인 경우.
---
## 5. Time-Series Split
- **특징**:
    - 시계열 데이터에 적합한 K-Fold 변형.
    - 과거 데이터를 학습 세트로, 미래 데이터를 검증 세트로 활용.
    - 데이터의 시간 순서를 유지하여 **미래 예측** 성능 평가.