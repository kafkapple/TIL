# Project setup
[ML Project Template / Structure setup](https://www.notion.so/ML-Project-Template-Structure-setup-12f596a3652f80b7b038fb009d8c4e61?pvs=21) 
# Side Project
https://github.com/kafkapple/github_grass_art.git
# Study
## 변수 변환 Overview
- **연속형 변수** 변환
    - **함수 변환**
        - **Log**
        - **제곱근**
        - **Box-Cox**
    - **Scaling**
        - **Min-Max (Normalization)**
        - **Standarization**
        - **Robust**
    - **구간화**
- **범주형 변수 변환 (Encoding)**
    - **One-Hot Encoding**
    - **Label Encoding**
    - **Frequency Encoding**
    - **Target Encoding**
---
## 변수 변환
### 1. **연속형 변수 변환**
- 연속형 변수는 값의 스케일을 조정하거나, 정규성을 확보해 모델 성능을 높이기 위해 다양한 방식으로 변환
- **함수 변환**
    - **Log 변환**: **비대칭** 분포의 데이터를 **정규 분포에 가깝게 변환**하여 데이터의 **스케일을 작게** 만듦으로써 편차 줄이고 모델의 회귀 성능 향상
    - **제곱근 변환**: Log 변환과 유사하나 효과가 약하며, 데이터가 0에 가까운 경우 주로 사용
    - **Box-Cox 변환**: Log와 제곱근 변환을 일반화한 방법으로, 특정 파라미터(λ, lambda)를 통해 다양한 형태의 파워 변환을 적용
        - λ=0일 때는 Log 변환
            - λ=1/2일 때는 제곱근 변환
            - 0<λ<1 인 경우는 **Power Transform**
                - 0과 1 사이의 양의 λ 값을 사용하는 Power Transform은 정규성 가정을 만족시켜야 하는 통계 분석이나 회귀 분석에 유용하게 사용
- **스케일링 (Scaling)**
    - **Min-Max 스케일링 (Normalization)**: 데이터를 0과 1 사이의 값으로 변환해 상대적인 크기를 조정.
    - **표준화 (Standardization)**: 평균을 0, 표준편차를 1로 변환하여 데이터의 분포를 표준화.
    - **로버스트 스케일링 (Robust Scaling)**
        - 중앙값, IQR 기준 변환
            - 중앙값과 거리를 IQR 로 나누기; x-xmed / IQR (x 75th - x 25th)
            - 중앙값 가까울수록 0, 멀수록 큰 값
            - IQR(75th - 25th)을 사용하여 이상치에 강건
- **구간화 (Discretization)**
    - 연속형 변수를 일정한 구간(bins)으로 나누어 **불연속 범주형 데이터**로 변환
    - 예) 연령을 10세 단위로 구간화하여 “10대,” “20대,” “30대”와 같은 범주형 데이터로 변환
### 2. **범주형 변수 변환 (Encoding)**
- 정의
    - 범주형 변수를 모델에 입력할 수 있는 형태의 수치 데이터로 변환
- 종류
    - **One-Hot Encoding**: 각 범주를 이진 벡터로 변환하여 각 범주를 독립적인 열로 표현
    - **Label Encoding**: 범주에 정수를 할당하여 각 범주를 숫자로 표현
    - **Frequency Encoding**: 각 범주의 빈도를 기반으로 값 할당
    - **Target Encoding**: 각 범주에 특정 타겟 변수의 통계량 (평균) 값을 할당하여 인코딩