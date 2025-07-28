# 📄 Python_Dotenv_Load

## ✨ 요약

Python에서 dotenv 라이브러리를 사용하여 환경 변수를 로드하는 방법을 학습함.

## 📍 학습 내용

### 1. 환경 변수 관리

#### 1.1 .env 파일의 역할

- 민감한 정보(API 키, DB 비밀번호 등)를 코드 외부에 저장함

- 개발 환경과 배포 환경 간 설정을 분리하여 관리함

- 코드의 이식성과 보안성을 높임

### 2. dotenv 라이브러리

#### 2.1 load_dotenv 함수

- .env 파일에 정의된 변수들을 시스템 환경 변수로 로드함

- find_dotenv()를 사용하여 .env 파일의 위치를 자동으로 탐색함

- 프로젝트 루트 디렉토리나 상위 디렉토리에서 .env 파일을 찾을 수 있음

### 3. 구현 및 활용

#### 3.1 환경 변수 로드 코드

- from dotenv import load_dotenv, find_dotenv를 통해 필요한 함수를 임포트함

- load_dotenv(find_dotenv())를 호출하여 환경 변수를 로드함

- 로드된 환경 변수는 os.getenv('VARIABLE_NAME')으로 접근 가능함