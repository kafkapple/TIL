# 241118📄 PortForwardingAndTensorBoard

SSH 포트 포워딩을 통한 원격 TensorBoard 접근 및 포트 설정 방법 학습.

### 1. SSH 포트 포워딩 (SSH Port Forwarding)

#### 1.1 로컬 포트 포워딩 (Local Port Forwarding)

- ssh -L [로컬포트]:[원격호스트]:[원격포트] [사용자]@[SSH서버] 명령어 구조

- 로컬 머신의 특정 포트를 통해 원격 서버의 특정 서비스에 접근

- 예시: ssh -L 3030:localhost:3030 [root@10.196.197.9](mailto:root@10.196.197.9 "mailto:root@10.196.197.9") (로컬 3030 -> 원격 3030 연결)

### 2. TensorBoard 실행 및 설정

#### 2.1 TensorBoard 기본 실행

- tensorboard --logdir=./logs_demo 명령어 사용

- 학습 로그 디렉토리 지정 (--logdir)

- 기본 포트 6006으로 실행

#### 2.2 TensorBoard 포트 및 호스트 설정

- --port 옵션을 통한 포트 변경

- --host 옵션을 통한 접근 허용 호스트 설정 (예: 0.0.0.0은 모든 IP 허용)

- 예시: tensorboard --logdir=./logs_demo --host=0.0.0.0 --port=6007 (포트 6007로 실행, 모든 IP 접근 허용)