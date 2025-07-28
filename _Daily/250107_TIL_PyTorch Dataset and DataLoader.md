PyTorch에서 데이터셋을 효율적으로 관리하고 모델 학습에 활용하기 위한 핵심 구성 요소인 Dataset과 DataLoader의 개념 및 사용법.
### **요약 표**

| 구성요소                   | 역할                  | 주요 메서드/옵션                                                                       |
| ---------------------- | ------------------- | ------------------------------------------------------------------------------- |
| `Dataset`              | 데이터셋 정의 및 개별 데이터 반환 | `__len__`, `__getitem__`                                                        |
| `DataLoader`           | 데이터를 배치 단위로 로드      | `batch_size`, `shuffle`, `num_workers`, `drop_last`, `pin_memory`, `collate_fn` |
| `torchvision.datasets` | 미리 정의된 데이터셋 제공      | `MNIST`, `CIFAR10`, `ImageFolder` 등                                             |

### 1. Dataset 개념 및 활용

#### 1.1 Dataset 정의

- torch.utils.data.Dataset 추상 클래스 상속

- __len__: 데이터셋 전체 크기 반환

- __getitem__: 인덱스에 해당하는 데이터 샘플 반환

#### 1.2 torchvision.datasets 활용

- 이미지, 텍스트 등 미리 정의된 데이터셋 제공

- MNIST, CIFAR10, ImageFolder 등

- PyTorch Dataset 클래스 상속 및 직접 사용 가능

### 2. DataLoader 기능 및 옵션

#### 2.1 DataLoader 역할

- Dataset 객체로부터 데이터 효율적 로드

- 학습 시 필요한 다양한 옵션 제공

- 필수 인자: dataset 객체

#### 2.2 주요 옵션

- batch_size: 미니 배치 크기 설정

- shuffle: 데이터 순서 무작위 섞기 (학습 시 True)

- num_workers: 병렬 데이터 로딩을 위한 서브 프로세스 수

- drop_last: 마지막 미니 배치 버릴지 여부

- pin_memory: CUDA 고정 메모리 사용 여부 (GPU 학습 시 속도 향상)

- collate_fn: 사용자 정의 미니 배치 구성 함수

### 3. DataLoader 활용 및 고려사항

#### 3.1 데이터 로딩 예제

- torchvision.datasets로 데이터셋 로드

- DataLoader 객체 생성 및 옵션 설정

- for 루프를 통한 배치 단위 데이터 접근

#### 3.2 핵심 사용 사례

- shuffle: 모델의 데이터 순서 의존성 방지

- num_workers: CPU 코어 활용 병렬 처리로 로딩 속도 향상

- drop_last: 배치 정규화 등 특정 레이어 사용 시 권장

- pin_memory: GPU 학습 시 데이터 전송 속도 최적화

### 4. **DataLoader 사용 예제**

```python
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1. 데이터셋 정의
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

dataset = datasets.MNIST(root="./data", train=True, transform=transform, download=True)

# 2. DataLoader 정의
dataloader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True,
    num_workers=4,
    drop_last=True,
    pin_memory=True
)

# 3. DataLoader를 이용한 데이터 반복
for batch_idx, (data, target) in enumerate(dataloader):
    print(f"Batch {batch_idx} | Data Shape: {data.shape} | Target Shape: {target.shape}")
    break

```