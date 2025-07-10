## **1. Docker 명령어**
### 1.1 **이미지 관리**
- **목록 확인**: `docker images`
- **다운로드**: `docker pull <이미지명>`
- **빌드**: `docker build -t <이미지명> <Dockerfile 경로>`
- **삭제**: `docker rmi <이미지 ID>`
### 1.2 **컨테이너 관리**
- **생성 및 실행**: `docker run [옵션] <이미지명>`
- **실행 중 목록**: `docker ps`
- **모든 목록**: `docker ps -a`
- **시작/중지**: `docker start/stop <컨테이너명/ID>`
- **삭제**: `docker rm <컨테이너명/ID>`
### 1.3 **컨테이너 내부 접속**
- **실행 중 컨테이너 접속**: `docker exec -it <컨테이너명/ID> /bin/bash`
- **터미널 환경 제공**: 컨테이너 실행 시 `/bin/bash` 또는 `/bin/sh` 옵션 사용.
### 1.4 **시스템 관리**
- **버전 정보**: `docker version`
- **전체 정보**: `docker system info`
- **디스크 사용량 확인**: `docker system df`
- **리소스 정리**:
    - **네트워크**: `docker network prune -f`
    - **볼륨**: `docker volume prune -f`
    - **전체 시스템**: `docker system prune -f`
### 1.5 **네트워크 설정**
- **포트 포워딩**: `docker run -p <호스트 포트>:<컨테이너 포트>`
---
## **2. Docker Compose**
### 2.1 **주요 명령어**
- **서비스 시작**:
    - 포그라운드: `docker-compose up`
    - 백그라운드: `docker-compose up -d`
- **서비스 종료**:
    - 기본: `docker-compose down`
    - 볼륨도 함께 제거: `docker-compose down -v`
- **서비스 재시작**:
    - 전체: `docker-compose restart`
    - 특정 서비스: `docker-compose restart <서비스명>`
- **로그 확인**: `docker-compose logs -f`
- **특정 서비스 빌드 및 실행**: `docker-compose up -d --build <서비스명>`
### 2.2 **설정 파일 활용**
- **기본 파일**: `docker-compose.yml`
- **환경 파일 적용**: `.env` 파일에서 민감 정보 관리 후 `env_file` 옵션 사용.
### 2.3 **캐시 및 빌드**
- **기존 캐시 활용**: `docker-compose up`
- **캐시 무시 빌드**: `docker-compose build --no-cache`
---
## **3. 이미지 및 파일 관리**
### 3.1 **COPY vs. Volume**
| **구분** | **COPY** | **Volumes** |
| --- | --- | --- |
| **장점** | 배포 간편 | 데이터 동적 관리 및 공유 |
| **단점** | 이미지 재빌드 필요 | 호스트 시스템 의존성 존재 |
| **사용 추천** | 배포 환경 (독립성 강화) | 개발 환경 (실시간 반영) |
---
## **4. 작업 흐름**
### 4.1 **이미지 빌드 및 실행**
- **이미지 빌드**: `docker build -t <이미지명> .`
- **컨테이너 실행**: `docker run -d -p <호스트 포트>:<컨테이너 포트> <이미지명>`
### 4.2 **Docker Compose 활용**
- **컨테이너 시작**: `docker-compose up -d`
- **변경 사항 반영**:
    - Dockerfile 수정: `docker-compose up --build`
    - 의존성 수정: `docker-compose build --no-cache`
### 4.3 **시스템 정리**
- **컨테이너 중지**: `docker stop $(docker ps -q)`
- **모든 컨테이너 삭제**: `docker rm $(docker ps -a -q)`
- **리소스 정리**: `docker system prune -f`
---
## **5. `docker stop` vs `docker pause`**
| **구분** | **docker stop/start** | **docker pause/unpause** |
| --- | --- | --- |
| **상태** | 컨테이너 종료 후 RAM 데이터 삭제 | 메모리에 작업 상태 유지 |
| **재시작 속도** | 느림 | 빠름 |
| **리소스 점유** | 중지 시 리소스 해제 | 리소스 지속 점유 |
| **예시** | 저장되지 않은 편집 내용 사라짐 | 작업 상태 그대로 유지 |