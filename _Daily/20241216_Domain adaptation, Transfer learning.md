**Domain Adaptation 개념**: 
- Transfer Learning이나 Fine-tuning과 달리, 라벨 없는 Test Domain에 적응하는 것. 
- 차이는 주로 "라벨 유무"와 "적응 대상(Train vs Test)"에 있음.

**Transfer Learning & Fine-tuning**:

- Transfer Learning
  - 대규모 소스 도메인(예: ImageNet)에서 학습된 사전 학습 모델을 가져와, 타겟 도메인(현재 과제의 Train 데이터)에 맞게 재학습(Fine-tuning)하는 과정.
- Fine-tuning
  - 모델 파라미터를 소스→타겟 도메인으로 적응시키는 단순한 접근
  - 타겟 도메인의 라벨이 있는 상태에서 진행.
  - 이 경우, 소스와 타겟 도메인이 상이하지만, 타겟 도메인(Train)의 레이블이 존재하고, 주로 소스→Train으로의 지식 이전에 초점.

**Domain Adaptation**:

- **Source Domain(Train 데이터)** 과 **Target Domain(Test 데이터)** 간의 분포 차이(shift)를 줄이는데 초점.
- 중요 포인트: Test 도메인에 대한 레이블이 없거나, Test는 단지 추론 대상일 뿐인데, 모델이 그 특성을 잘 받아들이게 하는 기법.
- Test 데이터 특징(분포, 스타일, 통계)을 모델에 반영하거나, 
- Feature Space에서 Source와 Target 차이를 줄이는 전략(MMD, CORAL, AdaBN 등)을 사용.
- 여기서 핵심은 "Test 도메인에 대한 라벨 없이, 단지 도메인 특성만 반영"하여 모델을 적응시키는 점.
- Fine-tuning과 달리, Test 라벨 없이 진행되므로 "Unsupervised" Domain Adaptation으로 많이 활용.