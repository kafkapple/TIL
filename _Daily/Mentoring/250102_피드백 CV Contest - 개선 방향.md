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

### 기타 다른 팀 분석 및 실험 참고

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

---

### 발표 시 추가 개선

- **Intro**에서 실험 목적과 접근 방법을 구체적으로 설명.
- Audience의 이해도를 고려한 간결하고 명확한 프레젠테이션.