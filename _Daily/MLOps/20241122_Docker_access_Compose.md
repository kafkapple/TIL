# Docker 접근

## docker exec:

```jsx
docker exec -it airflow-dags-container /bin/bash
```

- 실행 중인 컨테이너에 새로운 명령을 실행
- 컨테이너 외부에서 명령을 실행하지만, 내부에서 실행한 것과 같은 결과를 출력합
- 주로 컨테이너 상태를 디버깅하는 용도
- /bin/bash를 지정하지 않고 실행한 컨테이너에도 접근 가능

## docker attach:

- 실행 중인 컨테이너의 주 프로세스(PID 1)에 직접 연결
- 컨테이너의 표준 입출력(stdin, stdout, stderr)을 현재 터미널에 연결
- 컨테이너를 실행할 때 /bin/bash를 지정하지 않으면 bash shell에 접근 불가
- 웹 서버나 데이터베이스와 같은 백그라운드 프로세스에 attach하면 컨테이너가 비정상적으로 종료될 수 있어 주의가 필요

주요 차이점:

- exec는 새로운 프로세스를 생성하지만, attach는 기존 프로세스에 연결
- exec로 실행한 명령은 컨테이너 재시작 시 유지되지 않지만, attach는 기존 프로세스에 영향
- exec는 더 유연하고 안전하게 컨테이너를 조작할 수 있어 디버깅에 적합

# Docker Compose

```jsx
version: "2.3"
services:
  airflow:
    build: . # Dockerfile 위치
    container_name: airflow-dags-container
    ports:
      - "8080:8080" # 호스트의 8080 포트와 컨테이너의 8080 포트를 맵핑 (localhost:8080)
    volumes: # 호스트에서 dags 폴더 안에 dag를 정의한 파일을 생성하면 => 컨테이너에서도 실시간 확인이 가능
      - "./dags:/usr/local/airflow/dags"
    command: >
      bash -c "airflow webserver --port 8080 & airflow scheduler"
```

## Docker Compose 내의 여러 서비스 구분

예)

**`app`과 `airflow` 구분의 의미**

Docker Compose는 여러 서비스를 정의하고 동시에 관리

여기서 `app`과 `airflow`는 서로 **독립적인 역할을 가진 컨테이너**를 정의

**`app` 서비스**

- 앱의 코드와 관련된 환경을 제공
- 예: Flask/Django 서버, 백엔드 애플리케이션 등.

**`airflow` 서비스**

- Airflow를 실행하는 컨테이너
- 워크플로우 관리 도구로, DAG(Task)을 실행하고 스케줄링

**이 구분의 의미:**

1. 두 컨테이너는 서로 다른 목적을 수행
2. Compose는 여러 컨테이너를 동시에 관리하므로, 두 서비스를 함께 실행 및 네트워킹 가능
3. 필요하면 두 컨테이너가 통신하도록 설정할 수

# 기타

## **`bash -c`로 실행하는 것의 의미**

- `bash -c`는 Bash 셸에서 하나의 **명령어 또는 명령어 묶음을 실행**하기 위해 사용
1. 여러 명령어를 **한 줄로 연결**해 실행하려면 `bash -c`가 필요
2. 명령어를 따로 실행하면 컨테이너가 종료될 수 있으므로, `bash -c`로 묶어 실행

```
bash -c "airflow webserver --port 8080 & airflow scheduler"
```

- `airflow webserver`와 `airflow scheduler`를 **동시에 실행**하려는 의도
- `&`를 통해 백그라운드에서 실행되도록 설정.