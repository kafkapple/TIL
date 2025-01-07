
# 시계열 특성을 고려한 데이터셋 분리, 모델 성능 평가, 전처리 방법에 대한 멘토링

### 1. **시계열 데이터와 데이터셋 분리**

- **문제**: Train/Validation(Test) 셋의 분포가 시계열 특성으로 인해 크게 달라질 수 있음.
- **해결**
    - **Validation 점수 기준**: 모델 성능은 최종 Test 결과보다, **Validation 점수**를 기준으로 평가.
    - **Test 점수 신뢰도**: Test 점수에 지나치게 의존하지 말 것. (public 너무 믿지 말기)
        - 실제 평가 기준(private test)와 다를 수 있음. 샘플 일부만 공개
        - → kaggle shake up (실제 점수는, 이후에 private 셋으로 진행)
    - **추천 전처리**: Log Transform(특히, target 변수에 대해).

---

### 2. **Validation과 Test Metric 간 갭의 크기로 판단?**

- Validation과 Test 결과에 차이가 있는 경우:
    - **위험성**: 갭을 기준으로 모델을 선택하면 일반화에 실패할 위험이 있음.
        - 예) 갭이 큰 경우 일반화 덜 됨 < 낮으면 일반화 잘 됨
    - **우선순위**: 과도한 모델 복잡성보다는 Feature Engineering 중요

---

### 3. **Feature Engineering의 중요성**

- **EDA 필수**: 데이터의 특성을 파악하고, Feature Engineering은 데이터를 이해한 후 진행.
- **다중공선성 문제**: 다중공선성(Multicollinearity)을 사전에 확인.
- **Feature 수 제약**:
    - 권장 Feature 수: 약 300개 이내.
    - 규칙: `n_samples > n_features^2`를 만족해야 일반화 가능.

---

### 4. **스케일링과 전처리**

- **스케일링**
    - **Robust Scaling**: 연속형 변수에 Robust Scaling을 일괄적으로 적용.
    - Log Transform은 Target(y)에 적용 가능.
    - Train/Validation/Test 셋의 Y값 변환은 일관되게 처리(train-transform → test-transform).
    - 계산 시 원래 값으로 복원 필요.

---

### 5. **Train/Test 데이터 처리**

- **같이 처리 가능**: Train/Test를 합쳐서 전처리할 수 있는 경우.
    - Null 값 제거.
    - Encoding: Train/Test 클래스 간 차이를 고려해 함께 처리.
- **분리해서 처리 필요**:
    - Outlier 제거.
    - Scaling: 데이터셋을 분리한 상태로 각각 진행.

---

### 6. **추가 메모**

- 많은 Feature가 성능 향상에 기여하더라도 과도한 복잡성은 설명 가능성과 메모리 문제를 초래.
- 유지보수와 모델의 설명 가능성은 실무적으로 중요한 고려사항.