# 요약
## 1. **Train, Validation, Test Metric의 접근**
- **문제점**: Metric에 과도한 집착은 데이터 특성과 결과를 깊이 이해하는 데 방해가 됨.
- **해결책**: 정량적 평가 외에도 데이터의 정성적 관찰 및 validation set 구성의 중요성을 강조.
## 2. **EDA (Exploratory Data Analysis)**
- 주요 분석 요소:
    - 데이터 시각적 특성(`width`, `height`) 및 클래스 불균형 확인.
    - 데이터 샘플 직접 관찰 및 기본 베이스라인 코드 작성.
## 3. **적절한 의사결정**
- Validation set을 실제 test set과 유사하게 구성해 예측 정확도 향상.
- Test set 특성을 반영한 offline augmentation 전략 설계.
## 4. **Mix-Up Image 실험**
- 성능 저하 관찰 시 전략 수정 필요.
- 데이터 조건에 따른 Mix-Up 사용 여부 결정.
## 5. **팀 협업 및 발표 개선**
- **기록 및 공유**: 실험 기록 일관성 및 코드 공유 활성화.
- **Iterative 접근**: 문제 정의 → 실험 → 개선 반복.
## 6. **Augraphy 및 효율 개선**
- CPU 병목 현상 해결을 위해 offline augmentation 사용 권장.
---
## 7. **대회 일반**
### 데이터 분석 및 모델링 절차
- **데이터 검증 및 베이스라인 작성**:
    - 데이터 원본 확인 후 augmentation 전략 활용.
    - Validation과 리더보드 correlation 분석을 통해 개선.
- **이미지 처리 특화**:
    - Class별 약점을 파악해 rotate, mixup 등의 augmentation 추가.
    - 가설 → 실험 → 데이터/모델 재점검 과정 반복.
### 대회 설계
- **현업 연계성**: 문서 이미지 데이터 디지털화 트렌드를 반영한 문제 설계.
    - 금융, 의료, IT 등 다양한 산업군에서 활용 가능.
---
## 8. **문제 해결 프로세스**
- **문제 정의 및 해결**:
    - Evaluation metric이 문제 성과를 정확히 반영하는지 검토.
- **역량 강화**:
    - 연구 및 현업에서 문제 정의와 해결 중심의 사고를 강조.
---
## 9. **기타 참고 사항**
### 데이터 EDA
- Train/Test 분포 차이 시각화.
- EasyOCR, PaddleOCR로 텍스트 영역 검출 및 처리.
### 모델 및 실험
- **Optimizer**: AdamW, SGD 비교.
- **Scheduler**: Cosine, Sequential 비교.
- **Loss Function**: Cross Entropy, Focal Loss 실험.
- **Batch/Image Size**: 다양한 설정으로 실험.
- **Ensemble**: Temperature Scaling 등 방법 비교.
### 발표 개선
- 실험 목적과 방법을 명확히 전달.
- 간결하고 명확한 프레젠테이션 준비.
---
# 팀 발표
### 1. **Train, Validation, Test Metric에 대한 집착**
- **지양**: Metric에 과도하게 집착하지 않기. 숫자로 모든 문제를 설명하려는 경향에서 벗어나, 실질적인 데이터 특성과 결과를 더 심층적으로 분석.
    - 정량, 정성 (데이터 직접 눈으로 관찰) 평가 모두 필요.
- **대안**: 각 단계에서 실험 결과를 해석하고, metric 외의 관찰 가능한 패턴 및 문제점 도출.
    - test submission 결과와 correlation 경향성 있도록 validation set 구성하는 것 중요
### 2. **EDA (Exploratory Data Analysis)**
- **필수 분석 요소**:
    - 이미지 데이터의 `width`, `height` 등 시각적 특성 분석.
    - 클래스 불균형 여부 확인 및 시각화.
- **실행 제안**:
    - 데이터 샘플 10장을 확인하며 인사이트 도출.
    - 쉽게 반영 가능한 기본 베이스라인 코드 작성.
### 3. **적절한 의사결정**
- Metric 중심으로 의사결정하되, 데이터의 **분포 차이**와 **local validation set 난이도**를 고려.
- Validation set 난이도를 높여 실제 test set과 유사한 환경을 조성.
### 4. **Test Set 분석**
- Test set의 주요 특징 확인:
    - Noise, rotation, flip, color 변화 정도 확인.
- Augmentation 실험:
    - Test set과 유사한 패턴을 반영한 offline augmentation 전략 설계.
### 5. **Mix-Up Image 실험**
- Mix-Up 사용 시 성능 저하 관찰.
- 추가 실험 필요:
    - Mix-Up 전략 수정 또는 특정 데이터셋 조건에서 제외.
### 6. **발표 피드백 및 협업**
- **실험 기록**: 기록 방식의 일관성 유지.
- **코드 공유**: 팀 협업을 위해 코드 공유 플랫폼 적극 활용.
- **Iterative 분석**:
    - 지속적으로 문제를 정의하고 실험을 개선하는 반복적 접근.
### 7. **Augraphy 사용 및 병목 현상**
- Augraphy에서 CPU 사용량이 많아 병목 현상 발생.
- **개선**:
    - Online augmentation 대신 offline 처리로 효율 개선.
---
# 대회 일반
## 1. 데이터 분석 및 모델링 절차
### **데이터 원천 검증**
- 데이터 원본 확인 및 논리적 점검.
- 실험 가능한 사이트 정리 및 가장 쉽게 반영 가능한 사이트부터 베이스라인 작성.
- 대회에서 **augmentation 전략 활용** 강조.
- 기본 베이스라인을 코드화하여 내재화하고, 제출 후 결과 확인.
### **파라미터 및 검증**
- **하이퍼파라미터 튜닝**: Epochs, Learning rate, Backbones 등 간단히 변경 가능한 요소부터 조정.
- 어느 정도 리더보드 점수 갱신 데이터 누적되면, correlation 있는 validation set 정리
    - 하이퍼 파라미터를 변경했을 때 validation score와 리더보드 스코어 correlation이 중요
- 검증 데이터셋의 적합성과 Test 데이터 검토 후 **문제 정의 데이터셋 분석**.
- 이 과정부터 본격적인 EDA 시작!
    - Test 이미지(=정의된 문제를 잘 평가할 수 있는 데이터셋) 면밀하게 검토하여 인사이트 정리
### **데이터 분석**
- Correlation 있는 validation 확인 후 본격적인 EDA 및 실험.
- 데이터 계속 살펴보면서 여러 가설을 정리
- 주요 분석 요소:
    - 잘못된 라벨 정리 및 성능 향상 여부 확인.
    - Class imbalance 해결을 위한 oversampling
    - 가설 도출 후 검증.
### **이미지 처리 특화**
- 모델 결과 분석:
    - 모델 결과 예측 후 어떤 클래스를 잘 못하는지, 어떤 데이터의 점수 잘 못하는지 분석
    - 만약, rotate 이미지를 잘 예측 못하면, 학습할 때 rotate augmentation 추가
    - 만약, 텍스트 이미지에 왜 mixup된 이미지가 보인다, 학습할 때 mixup augmentation 추가
    - 결국 EDA를 통해 문제를 해결하기 위한 가설을 도출, 해당 가설 실험하면서 성능 향상에 대한 깊은 고민
    - 이런 과정이 되어야 다시 데이터를 보아야 할 수도 있고, 모델링을 보아할 수도 있음
    - 특정 클래스나 데이터에서의 약점을 파악하고 augmentation 전략 추가(예: rotate, mixup).
    - 문제 해결 가설 도출 → 실험 → 데이터/모델링 재점검.
- EDA를 중심으로 데이터와 모델 개선.
---
## 2. 대회 제작 과정
### **현업 연계성**
- 현업 문제를 다룰 수 있는 대회 설계 고민.
    - Kaggle과 달리 **실질적인 문제**를 다룰 필요성.
    - 의료/산업 데이터와 달리 **문서 이미지 데이터**의 실효성 강조.
    - 실 생활해보면, 도메인 상관없이 문서 이미지는 항상 다룸
        - 금융쪽에서도, 의료쪽에서도, 관공서에서도, 심지어 IT 회사에서도 문서이미지는 처리
        - 특히, 여러 대기업에서 아날로그 문서를 디지털화 하려는 작업이 최근에 많이 진행되고 있음
    - 문서 디지털화 작업의 트렌드를 반영한 대회 설계.
---
## 3. 중요한 경험과 문제 해결 프로세스
- **문제 해결 관점의 접근법**:
    - 대회 문제 정의 및 해결 필요성 분석.
    - ML/DL 어떤 모델로 풀어야 할까?
    - Evaluation metric이 문제 해결 성과를 정확히 반영하는가? → 메타 인지적 고민 필요
- **문제 정의 역량**:
    - 연구/현업에서 문제 정의 능력이 중요.
    - 연구와 제품 모두 **문제 해결 중심**으로 설계되어야 함.
# 기타 다른 팀 분석 및 실험 참고
### Data EDA
- **Train vs Test Set 분석**:
    - 데이터 분포 차이 시각화.
    - 샘플 데이터 비교 및 이상치(outlier) 파악.
- **텍스트 검출 및 추출**:
    - EasyOCR로 텍스트 영역 검출.
    - PaddleOCR로 텍스트 추출 및 추가 처리.
### 모델 파라미터 구성
- **Optimizer**:
    - AdamW, SGD 비교 실험.
- **Scheduler**:
    - Cosine, Sequential 비교.
- **Loss Function**:
    - Cross Entropy (CE), Focal Loss.
- **Batch Size, Image Size**:
    - 다양한 설정으로 실험.
### Ensemble 전략
- Temperature Scaling 등 Ensemble 방법 별 성능 비교.
### 발표 시 추가 개선
- **Intro**에서 실험 목적과 접근 방법을 구체적으로 설명.
- Audience의 이해도를 고려한 간결하고 명확한 프레젠테이션.