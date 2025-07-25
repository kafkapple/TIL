# 3강: 컴퓨터 비전 모델 구조 이해하기
[**3 컴퓨터 비전 모델 구조 이해하기**](https://www.notion.so/3-15e596a3652f808db3ccd84093b69b97?pvs=21) 
## 01 Backbone의 의미
1. **Visual Feature**
    - 컴퓨터 비전의 주요 태스크(classification, detection, segmentation 등)를 해결하기 위해 필요한, 이미지 내부의 핵심 정보를 담은 특징(Feature)을 의미
    - 이미지의 중요한 특성을 수치화하여 모델이 이해할 수 있도록 제공
2. **Backbone의 역할**
    - 다양한 레이어를 통해 입력 이미지에서 **압축된 Visual Feature**를 추출
    - 이후 단계(Decoder, 또는 추가 Encoder)에서 사용할 수 있도록 **중요 정보를 효율적으로 표현**
3. **Backbone의 구조**
    - 여러 개의 레이어로 구성, 레이어를 거치며 **점, 에지, 형태** 등의 다양한 레벨의 특징 추출
    - 예: CNN(Convolutional Neural Network)에서의 합성곱 레이어들을 연쇄적으로 쌓아 올린
---
## 02 모델의 구성
1. **Decoder의 역할**
    - Backbone이 추출하고 압축한 Feature를 **최종 태스크의 출력 형태로 변환**
    - 예:
        - **Classification** → 클래스 확률 출력
        - **Detection** → 바운딩 박스 및 클래스 확률 출력
        - **Segmentation** → 픽셀 단위 마스크 출력
2. **Encoder의 역할 (DETR 예시)**
    - Backbone에서 나온 Feature 또는 Image Patch들 사이의 관계를 학습
    - Transformer 구조의 Encoder-Decoder처럼, **자세한 맥락(Context) 정보**를 추가로 반영해 최종 성능 향상
---
## 03 Decoder의 역할 (상세)
1. **모델의 전체 구조**
    - **Backbone** → (필요 시 **Encoder**) → **Decoder**
    - Backbone: 이미지에서 Feature를 추출 후 **압축**
    - Decoder: 해당 Feature를 활용하여 **비전 태스크의 요구 형식**으로 결과를 도출
2. **Task별 Decoder 출력 예시**
    - **Fully Connected Layer (FC Layer)**
        - Classification 문제에서 디코더 역할 수행
        - Softmax와 함께 사용해 **클래스별 확률** 산출
    - **Detection**
        - 바운딩 박스(x, y, w, h) 예측 + 각 클래스별 확률
    - **Segmentation**
        - **픽셀 단위**로 영역 할당, 픽셀마다 어떤 클래스에 속하는지 예측
# 4강: Backbone 이해하기: CNN
[**4 Backbone 이해하기: CNN**](https://www.notion.so/4-Backbone-CNN-15f596a3652f80c88f8dc8aae35d7bdd?pvs=21) 
## 1. CNN 기본 구조
- **Conv Layer**: 입력 이미지를 필터(커널)와 컨볼루션해, 유용한 특징(feature) 추출
- **Activation**: ReLU 등 비선형성을 추가하여 모델의 표현력 극대화
- **Pooling Layer**: Spatial 차원을 축소하여 연산량 감소 및 위치에 대한 불변성 강화*예: Max Pooling, Average Pooling*
- **FC(Full Connected) Layer**: 최종 분류 등 목적을 위한 전결합 레이어
### Conv Layer 주요 파라미터
- **Filter(Kernel)**: 이미지 일부분을 훑으며 특성을 추출
- **Stride**: 필터 이동 간격
- **Padding**: 출력 크기 유지 목적 등으로 입력에 0 또는 임의 값 확장
---
## 2. AlexNet
- **ILSVRC(ImageNet) 대회에서 CNN 기반으로 최초 우승한 딥러닝 모델**
- **구조**
    - Conv → Pooling → Local Response Normalization(LRN) → Conv → … → FC
    - 총 8개 학습 가능 레이어(Conv 5 + FC 3)
    - 입력 이미지: 224×224×3
        224×224×3224 \times 224 \times 3
- **특징**
    - **ReLU 활성화 함수** 도입 (sigmoid 대비 빠른 학습)
    - **Overlapping Pooling**(풀링 영역 겹침)
    - **Local Response Normalization**(LRN): 주변 뉴런을 억제
        - 이후에는 Batch Normalization이 주로 사용
    - **Overfitting 방지**: Data Augmentation, Dropout
---
## 3. VGGNet
- **핵심 아이디어**: 큰 필터 대신 **작은 필터(3x3) 여러 개**를 쌓아서 깊은 구조(최대 19개 레이어) 형성
    - 동일한 receptive field(예: 7x7)라도 3x3 세 번 적용 시 **파라미터가 줄어듦**
    - 많은 레이어를 쌓을수록 **Nonlinearity**가 증가하여 표현력 향상
- **구조**
    - (Conv 3×3 × N) → Pooling → (Conv 3×3 × N) → Pooling → … → FC
        3×33 \times 3
        3×33 \times 3
- **장점**
    - 파라미터 효율적 사용, 표현력 증대
---
## 4. ResNet
- **등장 배경**: 깊은 네트워크(수십~수백 레이어)에서 발생하는 **최적화 난이도** 문제
    - 단순히 레이어 수를 늘리면 오히려 성능 저하(Overfitting과 무관)
    - **Gradient 소실/왜곡**으로 인해 학습이 어려워짐
- **Residual Connection**(잔차 연결)
    - H(x)=F(x)+x
    - **직접 H(x) 학습하기보다는, F(x) 라는 잔차(residual)만 학습**
    - 입력 x를 다음 레이어 출력에 단순 더해줌(Shortcut / Identity Mapping)
        xx
    - 깊어져도 그 이전 정보가 희석되지 않으므로 **더 쉬운 최적화** 가능
- **Bottleneck Layer(1x1 Conv)**
    - **채널 축소 및 복원**을 통해 계산량과 파라미터 수를 크게 줄여 깊은 네트워크를 구현
    - **Conv - BN - ReLU** 구조를 반복
- **Batch Normalization**(BN)
    - 각 레이어의 입력을 배치 단위로 정규화 → **더 빠른 학습, Gradient 흐름 개선, Regularization 효과**
---
## 5. EfficientNet
- **핵심 아이디어**: **MBConv(모바일 환경용 블록) + Squeeze-and-Excitation(SE) + Compound Scaling**
    1. **MBConv(Mobile Inverted Bottleneck Convolution)**
        - **Depthwise Separable Convolution**: Spatial 정보와 채널 정보를 분리하여 처리
            - Depthwise Conv: 각 채널별로 공간 컨볼루션
            - Pointwise Conv: 채널 정보(1x1 Conv)
        - **Squeeze and Excitation**: 채널별 중요도를 학습해 증폭/억제
    2. **Compound Scaling**
        - 모델의 **깊이(Depth)**, **너비(Width)**, **해상도(Resolution)**를 동시에 스케일링
        - 작은 검색(grid search)을 통해 비율(coefficient) 결정
        - 더 깊고 넓은 채널, 더 높은 해상도를 균형 있게 조정해 **정확도-연산량** 효율 극대화
---
### 정리
- **CNN 기본 구조**는 `Conv → Activation → Pooling → FC`로 이루어짐
- **AlexNet**: 대규모 이미지 분류 성공사례, Overlapping Pooling & Dropout & LRN으로 유명
- **VGGNet**: 작은 필터를 깊게 쌓아 성능 향상 및 파라미터 효율
- **ResNet**: Residual Connection으로 깊은 네트워크에서도 안정적 학습
- **EfficientNet**: MBConv + SE + Compound Scaling 조합으로 **효율**과 **성능** 모두 높임