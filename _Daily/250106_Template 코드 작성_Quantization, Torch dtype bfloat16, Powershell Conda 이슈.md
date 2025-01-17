

# Project

- 모듈 프레임워크 초점
  - Hydra 설정 관리
  - WandB(Weights & Biases)를 통한 실험 관리 및 시각화 기능
  - pytorch lighting
  - hugging face model manage

## Project_template 
- 딥러닝 실험을 위한 모듈화된 템플릿 코드 작성


## NLP Task Project Template 구현
https://paperswithcode.com/dataset/dialogsum

- Dataset
    
    https://github.com/cylnlp/dialogsum/tree/main/DialogSum_Data
    
    - 실제 대회 데이터셋, 위 데이터 한글로 번역해 제공
### template_nlp_sum (test_rouge)

### nlp

검증 완료 → 개선 중

- **DialogSum 데이터셋**
- **BART 기반 모델**
- ROUGE 스코어 사용
    - 생성된 요약문의 품질 평가

### summary


검증 완료. 


**데이터셋**

- **DialogSum 데이터셋**
    - 출처: GitHub cylnlp/dialogsum 저장소
    - 구조: 대화(dialogue)와 요약(summary) 쌍으로 구성
    - 파일:
        - train.json: 학습 데이터
        - val.json: 검증 데이터

**2. 모델**

- **BART 모델**
    - 기본 모델: facebook/bart-large-cnn
    - 크기: 약 400M 파라미터
- **T5 모델** (대체 옵션)
    - 기본 모델: t5-small
    - 크기: 약 60M 파라미터
    - 설정:

**파인튜닝 전략**:

- 그래디언트 체크포인팅 사용
- 선택적 레이어 동결
- 임베딩 레이어 동결 옵션

**4. 평가 메트릭**

- **ROUGE 점수**

<aside>
💡

</aside>

- 학습에 따른 metric 개선 확인

Evaluating model...Evaluating: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:05<00:00,  1.99it/s]Validation ROUGE scores: {'rouge1': 0.3878867728969686, 'rouge2': 0.1951162475308493, 'rougeL': 0.3183383168823225}

Validation ROUGE scores: {'rouge1': 0.41737868855929205, 'rouge2': 0.2105218297398614, 'rougeL': 0.3501939765357674}
# Study

https://github.com/kafkapple/project_template
## Quantization & dtype Precision

### Mixed Precision **혼합 정밀도란?**

- 혼합 정밀도는 **단일 모델에서 서로 다른 데이터 유형의 정밀도**를 사용하는 기법
    - 주로 **float32**와 **float16**(반정밀도) 두 가지를 혼합하여 사용
- **float32**:
    - 32비트 단정밀도. 
    - 기존 학습에서 주로 사용됨. 
    - 연산은 정확하지만 메모리와 연산 비용이 큼.
- **float16**:
    - 16비트 반정밀도. 
    - 메모리 사용량이 절반이지만, 오차나 언더플로우가 발생

### Torch `torch_dtype` 주요 옵션 설명 및 사용법

1. **`torch.float32` (기본값)**:
    - **특징**:
        - 32비트 부동소수점 형식.
        - 높은 정확도 제공.
        - 메모리 사용량이 큼.
    - **사용 예**:
        
        ```python
        
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float32  # 높은 정확도를 요구할 때
        )
        
        ```
        
2. **`torch.float16`**:
    - **특징**:
        - 16비트 부동소수점 형식.
        - 메모리 사용량 약 50% 감소.
        - 약간의 정확도 손실 가능.
        - GPU에서 연산 속도 향상.
    - **권장 시나리오**:
        - 대형 모델 (예: LLaMA, GPT 등)에서 GPU 메모리 절약이 필요할 때.
    - **사용 예**:
        
        ```python
        
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16,  # GPU 메모리 절약
            device_map="auto",         # 자동 장치 할당
            offload_folder="offload"   # 필요시 디스크로 오프로드
        )
        
        ```
        
3. **`torch.bfloat16`**:
    - **특징**:
        - Brain Floating Point 형식 (Google TPU에서 처음 도입).
        - `torch.float16`보다 더 안정적인 수치 연산 제공.
        - NVIDIA Ampere GPU (예: A100)에서 최적화.
    - **권장 시나리오**:
        - 대형 모델에서 수치 안정성이 중요한 경우.
    - **사용 예**:
        
        ```python
        
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16,  # 안정적인 연산
            device_map="auto"
        )
        
        ```
        

---

### **Quantization 8비트 양자화**

- **특징**:
    - 8비트로 모델 가중치를 양자화하여 메모리 사용량 크게 절감.
    - 적은 GPU 메모리로 대형 모델 실행 가능.
    - 약간의 성능 손실 발생 가능.
- **사용 예**:
    
    ```python
    
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        load_in_8bit=True,       # 8비트 양자화
        device_map="auto"
    )
    
    ```
    

---

### **LLaMA와 같은 대형 모델 권장 설정**

```python

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,  # GPU 메모리 절약
    device_map="auto",         # 자동 장치 할당
    offload_folder="offload"   # 디스크로 오프로드 가능
)

```

- **추가 옵션**:
    - **`device_map="auto"`**: 여러 GPU 또는 CPU 환경에서 자동으로 장치를 설정.
    - **`offload_folder="offload"`**: GPU 메모리 부족 시 디스크로 데이터를 오프로드.

## Powershell - conda 이슈

- conda 설치 위치 확인

- **새 프로필 파일 경로 설정**:
    - `$PROFILE` 값을 재정의.
    - PowerShell 세션에서 아래 명령을 실행
    
    ```powershell
    
    $PROFILE = "D:\MyPowerShellProfiles\Microsoft.PowerShell_profile.ps1
    ```
    
- **새 프로필 파일 작성 및 내용 추가**:
새 경로에 파일을 생성하고, 아래 코드를 추가
    
    ```powershell
    
    New-Item -ItemType File -Path $PROFILE -Force
    notepad $PROFILE
    ```
    
    **추가 내용**:
    
    ```powershell
    
    & "C:\Users\joon\miniconda3\Scripts\conda.exe" shell.powershell hook | Out-String | Invoke-Expression
    ```
    
- **PowerShell 실행 시 새 경로 참조**:
PowerShell을 재시작하면 새 위치의 프로필 파일이 적용