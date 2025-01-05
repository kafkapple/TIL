# 구현

## 부트캠프 수업

- Streamlit
    - webapp 으로 ML model serving
- Docker AirFlow
    - mnist dataset → model train inference

## 부동산 정보 크롤링

- streamlit
## Git TIL 보완

# Programming

## Workflow Management: AirFlow DAG

- **워크플로우(Workflow)**
    - 특정 작업을 수행하기 위한 일련의 작업 단계 또는 절차
    - 업무의 구조화와 효율화를 목표
- **Apache Airflow**
    - 데이터 파이프라인과 워크플로우를 관리하고 자동화하기 위한 python 기반 오픈소스 플랫폼
    - Airflow의 핵심 개념
        - **DAG(Directed Acyclic Graph)**
            - 이를 통해 워크플로우를 정의
            - DAG는 여러 작업(Task)으로 구성되며, 각 작업은 의존성을 가지고 있어 특정 순서로 실행
            - DAG와 작업(Task)은 Python 코드를 사용하여 정의
- **DAG**
    - **유향(Directed)**:
        - DAG 내의 각 작업은 명확한 실행 순서를 가지며, 한 작업에서 다른 작업으로의 흐름이 방향성
    - **비순환(Acyclic)**:
        - 작업 간의 흐름은 순환하지 않으며, 한 번 진행된 작업은 다시 되돌아가지 않음
    - DAG는 워크플로우 전체의 논리적 흐름을 정의하고, 이 흐름에 따라 개별 작업(Task)이 실행
        - 예를 들어, 데이터 수집 -> 데이터 처리 -> 데이터 저장의 순서로 구성된 데이터 파이프라인을 DAG로 정의
- **Operator, Task, Task Instance**
    - **Operator**
        - DAG 내에서 실제로 실행할 작업의 유형을 정의
        - 각 Operator는 특정한 작업을 처리하는 역할
    - **Task**
        - Operator로부터 정의된 실제 실행 단위
    - **Task Instance**
        - Task의 실행 인스턴스를 의미
        - 특정 시점에 Task가 실행될 때의 상태와 실행 기록
- 구성 요소
    - Scheduler: 워크플로우 스케줄링 및 트리거링
    - Executor: 작업의 실행과 리소스 할당
    - Web Server: UI를 통한 워크플로우 관리
    - Metadata Database: 워크플로우 및 작업 상태 저장
    - Worker: 실제 작업을 수행하는 프로세스

```
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
```

```python

task1 = PythonOperator(task_id='print_hello', python_callable=print_hello, dag=dag)

task2 = BashOperator(task_id='print_date', bash_command='date', dag=dag)

task3 = BashOperator(task_id='print_ls', bash_command='ls', dag=dag)

task1 >> [task2 >> task3]
```

## Docker

- **Docker**
    - 개발 환경과 운영 환경 간의 일관성을 보장하고, 설정이 간단해 많이 사용되는 방법
    - 여러 시스템에서 동일한 설정을 유지할 수 있어 팀 협업이나 프로덕션 환경 구축에 유리
- 강의에서 사용 동기
    - Airflow, windows 에서 사용 불가 → docker 로 경험

- **compose**
    - 이를 통해 도커 관리
    - compose up 만 하면 됨
- compose down 은 삭제니 주의. restart 로
- **image, container** 구분. 초반 실습은 이름에 둘 구분해 붙여줌
    - image build
    - container 는 image 기반으로

### Docker 핵심 명령어

```css
docker-compose up --build
(-d 옵션은 백그라운드에서 실행)
(build + run 포함)

-실행 중 컨테이너 확인
docker-compose ps

- 컨테이너 접속
docker exec -it <container_name> /bin/bash

- 종료
docker-compose down

- 잠시 멈춤 (10초 정도 여유 필요; 컴퓨터 끌 때 )
docker stop <container_id>
docker start <container_id>
docker restart
docker container rm 
- 현 컨테이너 상태로 새로 이미지로 docker 저장할수도
docker commit
```

- docker 잘 쓰는지 보는 법?
    - linux 가벼운 버전으로
    - compose  yml있어야

## web crawling 웹 크롤링

개발자 도구를 사용하여 웹 콘텐츠의 Fetch/XHR 요청을 필터링하고 curl 명령어를 이용해 자동화하는 방법

- api 제공안해도, 직접 떼어 fetch 가능

1. 크롬 개발자 도구 열기: F12 키를 누르거나 브라우저 메뉴에서 "더 보기 도구 > 개발자 도구"를 선택
2. 네트워크 탭으로 이동: 개발자 도구에서 "Network" 탭을 선택
3. Fetch/XHR 필터 적용: 네트워크 탭에서 "Fetch/XHR" 옵션을 선택하여 Fetch 또는 XHR 요청만 필터링
4. 원하는 요청 선택: 필터링된 요청 중 자동화하고자 하는 요청을 찾아 클릭
5. curl 명령어로 복사: 선택한 요청을 우클릭하고 "Copy > Copy as cURL" 옵션을 선택하여 curl 명령어 형식으로 복사
6. 스크립트 작성: 복사한 curl 명령어를 스크립트(예: Bash, Python)에 붙여넣고 필요에 따라 수정

- 설정-기타도구-개발자 도구
    - 네트워크 탭
        - fetch /XHR 필터 걸기 (데이터 요청 관련)
- 대상 우클릭 후 copy curl (bash)
- curl converter
    - https://curlconverter.com/
- 복사한 curl 붙여넣으면 python code 완성
- 예시 대상
    - 맛집, 네이버 부동산

# 기타 상식 및 여담

- 페이로드(payload)
    1. **데이터의 핵심**: 페이로드는 전송의 근본적인 목적이 되는 데이터
        - 헤더, 메타데이터, 프로토콜 오버헤드 등을 제외한 **실제 전송 목적이 되는 데이터 부분**
    2. **구조**: 일반적으로 JSON이나 XML 형식으로 구조화
    3. **위치**: 데이터 전송 구조에서 주로 Body 부분에 포함
- no code 툴
    - 서비스 하기 좀 그럼 → MVP tool
    - error 잦고 디버깅 어렵