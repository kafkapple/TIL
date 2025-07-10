# ML Pipeline
### **1. Data Preprocessing**
- **EDA (Exploratory Data Analysis)**: 데이터의 특성을 파악하고 문제점 식별.
- **Issue Handling**:
    - **Missing Values**: 데이터 누락 해결.
    - **Outliers**: 제거, 대체 또는 스케일링으로 처리.
- **Variable Processing**:
    - **Continuous Variables**: 함수 변환, 스케일링, 구간화.
    - **Categorical Variables**: One-Hot Encoding 등 적절한 변환.
---
### **2. Feature Engineering**
- **Derived Variable Creation 파생 변수 생성**:
    - 문제 도메인 지식을 반영한 변수 추가.
    - 단순 합성보다 데이터의 맥락을 고려한 변수 설계.
- **Variable Transformation 변수 변환**:
    - 함수 변환 (e.g., 로그, 루트 등).
    - 변수 간 상호작용 및 통계 기반 변수 생성.
    - 시간 변수 활용 및 분할.
- **Importance**:
    - 성능: 모델의 예측 성능 향상.
    - 해석: 도메인 지식 기반으로 더 인간 친화적 분석.
    - 메모리: 정보 손실 최소화 및 전처리 속도 향상.
---
### **3. Feature Selection**
- 문제에 유의미한 변수만 선택해 모델 효율성 개선.
#### Filter method
- 통계적 기법 활용
  - Variance Threshold: 분산이 특정 기준보다 낮은 변수 제거.
  - Correlation Threshold: 상관계수가 높은 변수 중 하나 제거.
#### Wrapper method
- 모델 성능 기반
  - Sequential Feature Selection (SFS)
  - Recursive Feature Elimination(RFE)
#### Embedded method
- 모델 훈련 과정에서 중요도 기반
  - Feature importance
---
### **4. Model Selection**
- **Purpose-based Model selection**:
    - 문제에 적합한 알고리즘 채택.
- **Hyperparameter Tuning**:
    - 하이퍼파라미터 조정을 통한 최적화.
- **Dataset splitting**:
    - Train/Validation/Test로 데이터 분리.
- **Evaluatin and Validation**:
    - 모델 성능 평가(Evaluation Metrics).
---