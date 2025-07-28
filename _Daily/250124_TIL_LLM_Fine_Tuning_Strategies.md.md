# LLM_Fine_Tuning_Strategies

# 📄 LLM_Fine_Tuning_Strategies

대규모 언어 모델(LLM)의 효율적인 Fine-tuning 전략과 자원 제약 환경에서의 활용 방안.

### 1. LLM Fine-tuning 접근 방식

#### 1.1 Custom Classifier

- **적용 상황**: 충분한 데이터셋, 특정 Task 성능 최적화, 대량 배치 추론

- **특징**: Task-specific 모델, 모든 파라미터 학습(Fine-tuning)

- **장점**: 높은 Task 성능, 안정적인 추론

#### 1.2 Prompt Template

- **적용 상황**: 데이터셋 부족, 빠른 프로토타이핑, Zero/Few-shot 학습, Structured Output

- **특징**: 사전 정의된 템플릿, Prompt Engineering 필요

- **장점**: 적은 데이터로 활용, 유연한 제어

### 2. Fine-tuning 세부 기법

#### 2.1 파라미터 효율적 학습 (Parameter-Efficient Tuning, PET)

- **LoRA (Low-Rank Adaptation)**: Custom Classifier에 일부 Layer Fine-tuning, 작은 Sub-layer 업데이트

- **Adapters**: 모델 파라미터 고정, Task-specific Layer 추가 학습

- **Prefix Tuning**: Prompt Template 응답 형식 제어, Pre-trained Prompt 추가

#### 2.2 모델 경량화 및 전이 학습

- **Knowledge Distillation**: 큰 Teacher 모델에서 작은 Student 모델로 정보 전이, 경량화된 모델 학습

- **qLoRA**: 4비트 모델 압축, GPU 메모리 사용량 대폭 감소 (주로 추론에 효과적)

### 3. Fine-tuning 환경 및 고려사항

#### 3.1 Tokenizer 및 Special Tokens

- **Special Tokens**: eos, bos, pad, sep 등 문장 구조 이해 보조

- **Tokenizer**: 모델별 규칙 상이, Fine-tuning 시 업데이트 필요성

#### 3.2 Fine-tuning 전략 및 최적화

- **하드웨어 제약**: RTX 3090 (70B LLM qLoRA), 7B SLM (마지막 2-3 Layer unfreeze)

- **앙상블**: Short, Mid, Long Sample Ensemble로 최종 결과 향상

- **최적화**: Batch Size 조정, Mixed Precision 활용 (GPU 메모리 최적화)

#### 3.3 PyTorch Lightning 업데이트

- **Hook 변경**: validation_epoch_end -> on_validation_epoch_end

- **목적**: 명확한 Task 주기 및 이벤트 기반 로직 지원

#### 3.4 RTX 3060 (12GB VRAM) 70B 모델 사용 불가

- **메모리 부족**: 70B 모델은 최소 40GB 이상 VRAM 필요

- **대안**:

- **LoRA/qLoRA**: 메모리 절감 (12-15GB 수준으로 축소 가능)

- **CPU 오프로드 + GPU 분산**: Accelerate 활용 (성능 저하)

- **Deepspeed ZeRO / Tensor Parallelism**: 단일 GPU 제한적

- **클라우드 활용**: AWS EC2, Google Cloud 등 고사양 GPU 인스턴스 (A100, H100)

### **세부 기법 및 적용 사례**

|**기법**|**적용 상황**|**특징**|
|---|---|---|
|**LoRA**|Custom Classifier에 일부 Layer만 Fine-tuning 필요 시 사용|기존 모델의 작은 Sub-layer만 업데이트하여 효율적 Fine-tuning 가능.|
|**Knowledge Distillation**|큰 Teacher 모델에서 작은 Student 모델로 정보 전이 필요 시|Student 모델이 Teacher의 성능을 모방하며, 경량화된 모델을 학습 가능.|
|**Adapters**|모델 파라미터를 고정하고 Task-specific Layer만 추가해야 할 때|기존 모델의 가중치를 유지하며, 작은 추가 Layer를 학습하여 새로운 Task에 적응 가능.|
|**Prefix Tuning**|Prompt Template 응답 형식을 더욱 강제하고 제어가 필요할 때|모델의 입력에 Pre-trained Prompt를 추가하여 Fine-tuning 없이 형식적 응답 제어 가능.|