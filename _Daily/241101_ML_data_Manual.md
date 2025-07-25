# 메뉴얼 작업
- GPU pytorch setup 가이드 리뉴얼
    - [GPU CUDA Torch setup](https://www.notion.so/GPU-CUDA-Torch-setup-131596a3652f809d8ef5fd4720d9bdf0?pvs=21)
- Github Actions for TIL
    - [Github Actions - TIL setup](https://www.notion.so/Github-Actions-TIL-setup-131596a3652f80dab75ede026f8277c6?pvs=21)
- Emotion-LLama
    - [Emotion-LLaMa Setup](https://www.notion.so/Emotion-LLaMa-Setup-131596a3652f80cc8cfbdc37ea5e5688?pvs=21)
# 구현
- Emotion-llama https://github.com/kafkapple/Emotion-LLaMA
    - 기능 추가
        - system OS 관계 없이 config path normalize 기능 추가 구현
    - 테스트
        - demo app 로컬에서 성공
        - sample 영상 정성적 test
# 공부
## I. ML 개요
**`DL $\subset$ ML $\subset$ AI`**
### 1. **인공지능 (Artificial Intelligence, AI)**
- **정의**
    - 인간의 학습, 추론, 지각 능력을 **인공적으로 구현 
    →** 컴퓨터가 특정 문제를 스스로 해결할 수 있도록 하는 기술
### 2. **머신러닝 (Machine Learning, ML)**
- **정의**
    - 사람이 직접 코딩하지 않고, 데이터를 통해 모델이 **패턴과 규칙을 학습**하여 문제를 해결
    - 기존 어려운 고수준, 추상적 기능 직접 구현
- **방법**
    - **함수 공간 정의**: 특정 작업을 수행하는 함수 모델을 설정하고, 이 함수의 **파라미터**를 조정하여 학습함.
    - **손실 함수 최적화**: 파라미터를 조정하여 함수가 데이터를 잘 설명할 수 있도록 **손실 함수**(예측과 실제 값 간의 오차)를 줄여 나감.
    - **학습 과정**: 데이터 사용해 **오차**를 측정하고, 이를 최소화하도록 파라미터를 조정하며 점진적으로 모델을 개선.
### 3. **딥러닝 (Deep Learning)**
- **정의**
    - 다층의 **심층 신경망(Deep Neural Networks)**을 사용하는 머신러닝의 한 분야
    - 복잡한 패턴 학습과 높은 수준의 문제 해결을 가능하게 함.
- **특징**
    - **다층 구조**: 여러 층의 노드(뉴런)로 이루어진 네트워크로, 각 층은 이전 층의 출력을 입력으로 받아 **추상적 특징**을 점진적으로 학습함.
    - **파라미터 수**: 많은 수의 파라미터(가중치)를 가지며, 이를 통해 다양한 기능을 구현하고 고도화된 학습이 가능함.
## II Data 데이터 / Variable 변수 타입
### 1.1. **형태에 따른 분류**
- **정형 (Structured)**: 표 형태로 정리된 데이터, 분석에 용이함.
    - **예시**: 데이터베이스 테이블, CSV 파일, 엑셀 스프레드시트 등.
- **비정형 (Unstructured)**: 고정된 형식이 없고, 텍스트, 이미지, 오디오 등 다양한 형태.
### 1.2. **데이터 특성에 따른 분류**
- **정량 (Quantitative)**: 수치로 측정 가능한 데이터.
- **정성 (Qualitative)**: 범주나 특성으로 표현되는 데이터.
### 1.3. 세부 분류
1. **Structured Data (정형 데이터)**
    - **Quantitative (정량)**
        - **Numerical (수치형):** 숫자로 측정 가능
            - **Continuous (연속형)**
                - 실수로 표현되며, 값의 범위 내에서 무한히 나눌 수 있음
                - 예) 키, 무게
            - **Discrete (이산형)**
                - 정수로 표현되며, 특정 개수로 셀 수 있음
                - 예) 제품 개수, 학생 수
    - **Qualitative (정성)**
        - **Categorical (범주형):** 숫자가 아닌 특정 범주나 속성을 표현
            - **Nominal (명목형)**
                - 순서가 없는
                - 예) 성별, 국가
            - **Ordinal (순위형)**
                - 순서가 있는
                - 예) 만족도 등급, 교육 수준
2. **Unstructured Data (비정형 데이터)**
    1.  고정된 형식이 없고, 비구조적인 데이터
    2. 텍스트, 이미지, 오디오 등 다양한 형태
    3. **추가적인 전처리** 필요
    - **Quantitative (정량)**
        - 예) 이미지의 픽셀 값, 오디오 주파수
        - 비정형 데이터이지만, 픽셀 값이나 주파수 같은 수치 데이터를 포함할 수
    - **Qualitative (정성)**
        - 예) 텍스트, 소셜 미디어 게시글, 오디오 텍스트
        - 주관적인 감정이나 질적 특성을 표현
## III Data의 수치적 표현 방법
### 1. **Structured Data (정형 데이터)**
- **Categorical (범주형 데이터)**
    - 범주형 데이터는 **각 범주에 고유한 인덱스를 할당**하여 표현
    - 이 인덱스는 임의적일 수 있으며, 범주 간의 순서를 의미하지는 않음
        - 예시: 성별 (남성=0, 여성=1), 제품 종류 (A=1, B=2, C=3)
    - **One-Hot Encoding**
        - 범주형 데이터를 벡터로 변환할 때 사용하는 방법
        - 각 범주를 이진 벡터로 표현
### 2. **Unstructured Data (비정형 데이터)**
- **Text (텍스트)**
    - **Token Indexing**
        - 텍스트 데이터를 단어나 서브워드 단위로 쪼개어 각 토큰에 고유한 인덱스를 할당
    - **Embedding (임베딩)**
        - 텍스트 데이터의 의미를 표현하기 위해 각 토큰을 고차원 벡터 공간에 매핑.
        - 예) Word2Vec이나 BERT
- **Image (이미지)**
    - **길이 3의 벡터 (RGB)**
        - 각 픽셀의 색상을 RGB (Red, Green, Blue) 채널로 표현
        - 각 채널 값은 0에서 255 사이의 정수
    - **Resolution (해상도)**
        - 이미지의 가로(Width)와 세로(Height) 픽셀 수로 표현
- **Video (비디오)**
    - **Temporal Resolution (시간 해상도)**
        - 비디오의 프레임 속도(fps: frames per second)로 표현 (15~30fps)
    - **RGB Channel / Spatial Resolution**
        - 비디오의 각 프레임이 이미지이므로, 이미지와 동일
- **Audio (오디오)**
    - **Amplitude Range (진폭 범위)**
        - 음성 신호의 크기를 표현
        - 일반적으로 -1에서 1 사이의 부동소수점 값으로 저장
    - **Sampling Rate (샘플링 주파수)**
        - 아날로그 음성 신호를 디지털로 변환할 때 초당 샘플링하는 횟수
        - 일반적으로 44.1kHz 또는 48kHz로 설정
            - 이는 가청 주파수 범위(20Hz~20kHz)를 초과하는 주파수까지 표현할 수 있도록 Nyquist 이론에 따라 설정
    - **Bit Depth (비트 깊이)**
        - 각 샘플의 세부 표현 정확도를 나타내며, 일반적으로 16비트 또는 24비트로 저장
        - 비트 깊이가 높을수록 소리의 다이나믹 레인지 표현 상승