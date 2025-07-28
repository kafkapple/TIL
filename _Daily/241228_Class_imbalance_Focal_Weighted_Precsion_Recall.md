### **1. 주요 기법과 목적**
| **기법** | **주요 목적** |
| --- | --- |
| **Weighted Sampler** | 소수 클래스 샘플 비율 증가 → **Recall**(재현율) 개선. |
| **Focal Loss** | 어려운 샘플에 초점 → **Recall 직접 개선**, **Precision 간접 개선 가능**. |
| **Data Augmentation** | 소수 클래스 데이터 다양성 증가 → 클래스 불균형 완화 및 모델 일반화 성능 향상. |
| **α, γ 추가 조정** | α: 클래스 중요성 강조, γ: 어려운 샘플에 초점 조정 → 손실 함수 최적화. |
| **하이퍼파라미터 튜닝** | 학습률, α, γ 등 최적화를 통해 성능 극대화. |
| **도메인 적응 기법** | 학습/실제 도메인 간 분포 차이를 줄여 일반화 성능 향상. |
---
### **2. Focal Loss와 평가 지표의 관계**
- **Recall**:
    - 어려운 샘플(FN 감소)에 집중하여 **직접 개선**.
    - FN 감소를 통해 긍정 클래스를 더 잘 예측.
- **Precision**:
    - FP 감소 가능성으로 **간접 개선** 가능.
    - Precision 개선이 주요 목표라면 **Threshold 조정, Class Weight** 등의 기법과 병행 추천.
| **지표** | **Focal Loss의 효과** |
| --- | --- |
| **Recall** | 어려운 샘플에 초점(FN 감소) → **직접 개선**. |
| **Precision** | FP 감소 가능 → **간접 개선 가능**. Precision 개선에는 보조 기법 필요. |
---
### **3. 전략의 우선순위**
| **상황** | **1순위** | **2순위** | **3순위** | **추가 조정** |
| --- | --- | --- | --- | --- |
| **Recall이 낮은 경우** | Weighted Sampler | Focal Loss | Data Augmentation | α, γ 추가 조정 |
| **Precision이 낮은 경우** | Focal Loss | Data Augmentation | Weighted Sampler | α, γ 추가 조정 |
| **Recall & Precision 모두 낮음** | Weighted Sampler + Focal Loss | Data Augmentation | 하이퍼파라미터 튜닝 | α, γ 추가 조정 |
---
### **4. 적용 방안 요약**
1. **Recall 개선**:
    - **Weighted Sampler**로 소수 클래스 샘플 비율 증가.
    - **Focal Loss**로 어려운 샘플에 초점.
    - **Data Augmentation**으로 데이터 다양성 강화.
2. **Precision 개선**:
    - **Focal Loss**로 FP 감소 유도.
    - **Data Augmentation**으로 클래스 간 구분 명확화.
    - 필요 시 **Weighted Sampler** 보조.
3. **Recall & Precision 모두 낮음**:
    - **Weighted Sampler + Focal Loss**를 함께 적용.
    - **Data Augmentation**과 **하이퍼파라미터 튜닝** 병행.
---
### **결론**
- Focal Loss는 **Recall 개선에 직접적**, Precision에는 **간접적 효과**.
- Weighted Sampler는 데이터 단계에서 **소수 클래스 비율 증가**로 Recall에 유리.
- Precision 개선이 주요 목표일 경우 **Focal Loss와 추가 기법**(Threshold 조정 등)을 병행하는 것이 적합.