# Markdown_image_embed_Convention_LLM_mermaid

# Markdown

- 트리 구조를 plaintext 코드 블록으로 감싸기

- 전체 마크다운을 markdown 으로 감싸기

## Link Embed

- link 삽입

- [caption](url

- image 삽입

- ![이미지 설명](이미지_URL)

- Markdown 자체로는 이미지 크기 조정을 지원하지 않지만, HTML을 이용하면 가능

- HTML 사용:

```

html

<img src="https://example.com/image.png" alt="이미지 설명" width="500"/>

```

- 예시 (Markdown과 HTML 혼용):

```

markdown

# My Project

<img src="images/example.png" alt="My Logo" width="300">

```

# Convention

- 대문자 변수 표기: e.g., API_KEY

- 상수, 고정 값 의미

- mlflow server 등에서 127.0.0.1 의미?

- localhost 로 해도 무방하나, 가끔 아닌경우 있어 명시하는게 좋음

## pydantic

- Python을 위한 강력한 데이터 검증 및 설정 관리 라이브러리

- 주로 유형 주석과 함께 작동하도록 설계

- 데이터가 특정 유형과 제약 조건을 준수하는지 확인하는 프로세스를 간소화하여 데이터 검증이 중요한 FastAPI와 같은 애플리케이션에서 특히 유용

- FastAPI에서 요청 및 응답 검증을 위해 많이 활용

# 기타

- mermaid chart

- claud 로 초안 작업 → mermaidchart.com

- 서식 제거 붙여넣기

- ctl+shift+v

- LLM 학습시 추천

- 양자화

- vLLM: 메모리 효율관리

- 라마 블로썸 + RAG