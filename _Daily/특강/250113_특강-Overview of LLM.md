## I. Prompt Engineering

- **Transformer 구조 무거운 이슈**
    - Encoder와 Decoder를 분리해, 목적에 따라 각각 최적 활용해 보자
- **Encoder: BERT**
    - Masked Language Modeling 기반
    - 과거에 빠른 성능 향상으로 큰 인기
- **How to train (기본 개념)**
    - Next word prediction(언어모델) → 비지도학습
    - Zero-shot learning 가능
- **Decoder: GPT-3**
    - In-context learning
        - Zero-shot보다는 “문맥 속에서” 예시를 주고 해결 → 모델 파라미터 업데이트 없이 즉석 추론
- **InstructGPT**
    - Steerability(조정 가능성) 개선 → 주어진 지침에 맞춰 답변하도록 학습
- **Alignment Tuning**
    - 모델이 사람 의도(가이드라인)에 부합하게 대답하도록 조정
    - RLHF(인간 피드백 기반 강화학습) 방식 활용
- **Prompt Strategies**
    - **Clarity with delimiters**
        - 구분자(예: “””) 사용해 사용자 입력/요청을 명확히 구분
            - e.g., as a bullet point lit of the most important points
            
            text: “””
            
            {input here}
            
            “””
            
    - Understanding about LLMs
        - 실시간 정보 모르므로, 정보 추가로 줘서 요청
    - **Position of information**
        - 중요한 정보를 Prompt 앞/뒤 어디에 위치시킬지 결정
    - **Chain of Thought (CoT)**
        - 중간 사고 과정을 텍스트로 풀어나가는 기법 (내뱉게)
        - think step by step
    - **Program-of-Thought (PoT)**
        - 복잡한 수학 문제 등에서 “프로그램처럼” 단계적 접근

---

## II. RAG (Retrieval-Augmented Generation)

- **동기(Motivation)**
    - LLM은 최신 정보나 구체적 사실에 약함 → RAG는 검색으로 이를 보완
    - “Hallucination” 현상 방지를 위해 외부 문서(지식) 참조
- **Chunking & Embedding**
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/00c8f8ca-9b9e-47d7-a22a-d972f43cd460/6c155928-a711-4bdf-8c50-a0659dd8f229/image.png)
    
    - 문서를 일정 크기 단위로 쪼개고(Chunking), 각 덩어리에 대한 임베딩 생성
    - 고정 길이 vs 문서 단위 vs 문장 단위 vs 의미 단위 등 다양한 방법 존재
        - fixed-size chunking
        - document based chunking
            - e.g., by sentence
            - by markdown syntax
        - semantic chunking
            - 문제: 길이 달라짐
            - 자체로 어려운 task
- **Retrieval Strategies**
    - **Hybrid search**
        - Sparse(전통 TF-IDF 등) + Dense(임베딩 기반) 검색 조합
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/00c8f8ca-9b9e-47d7-a22a-d972f43cd460/a2d802ae-6546-480b-b012-4466423e7995/image.png)
    
    - **Query expansion**
        - 사용자 쿼리를 여러 형태로 확장해 검색 범위 확보
        - 
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/00c8f8ca-9b9e-47d7-a22a-d972f43cd460/dbc5c499-0372-4f02-9dcf-999e8f986cb3/image.png)
        

---

## III. Instruction Tuning

- **User와의 대화 데이터 기반 지도학습**
    - 사용자 입력과 정답(응답) 쌍으로 모델을 지도학습(Supervised)
        - user input 에 masking (only response loss)
    - “어떻게 고품질 Instruction(지시문)을 만들고 수집할 것인가?”가 핵심
- **합성(Synthetic) 데이터 기법**
    - **Self-Instruct**
        1. 초기 시드(seed) 주고
        2. 분류( task 유형; classification 특히 구분) → 
        3. Response 응답 생성 → 다시 질문 생성 … (반복/확장)
    - **Orca**
        - 맥락 정보를 풍부하게 주어 고도화
    - **Self-alignment**
        - 웹에서 가져온 문서(예: 위키)를 답변으로 간주 → 역으로 질문 생성
    - **SAIL (Search Augmented Instruction Learning)**
        - 합성 데이터 방법론과 다 똑같은데 차이는
            - 검색된 실제 정보 같이 넣어주고 response 학습하게
    - **WizardLM**
        - initial seed → LLM → generation
        - “Evolving” 방식으로 난이도·다양도를 높여가며 질문/답변 생성, 오류 제거 후 학습
            - in-depth 난이도 높이는
            - in-breadth 유사 난이도 생성 → 다양성 향상
            - elimination → evolving 한 결과를 다시 LLM 에서 학습하기 적절한지 물어봄 → 오류 있음 제거

---

## V. Alignment Tuning

- **Instruction Tuning vs Alignment**
    - Alignment는 모델 응답은 생성하고, 이에 대한 인간 “선호도”를 학습
        - 더 간단함
            - 상대적 선호도만 인간이 레이블링 하면 됨
        - → 모델이 사회적·윤리적 기준을 지키도록
    - RLHF(RL from Human Feedback)
        - 사람의 평점(rating)을 활용한 강화학습
    - RLAIF(AI Feedback)
        - 사람 대신 AI가 rating을 생성해 활용
- **SFT (Supervised Fine-Tuning)**
    - **DPO(Direct Preference Optimization)**
        - PPO(정책 최적화) 아이디어를 변형한, 현재 많이 활용되는 방식
            - 기존 RL PPO 수식에서 출발, 탄탄
    - **ULMA**
        - Point-wise 방식으로 Cross Entropy만으로도 학습 가능
            - 굳이 preference 아니어도 학습 가능하도록 cross entropy 형태로 변환
    - **Self-rewarding**
        - 모델이 자체적으로 reward 점수를 생성하며 학습

---

# 기타

- model collapse 이슈
    - 합성 데이터 만드는 모델, ( 사이즈 더 크게)
    - 실제 모델 다르게 구분

→ 큰 모델 능력을 작은 모델에 distillation 하는 셈

- COCONUT 같은 latent space embedding 수준에서의 BFS CoT 연구?
    - reasoning 쪽 연구는 활발.
    - latent space 쪽도 연구 존재는 함

### 정리 요약

1. **Prompt Engineering**
    - Transformer 구조를 이해하고 Encoder/Decoder를 목적별로 활용
    - BERT, GPT-3, InstructGPT 등을 통해 다양한 훈련 방식(MLM, next-word prediction, in-context learning)과 Steerability 개념 이해
    - RLHF 등으로 모델을 특정 방향으로 조정(Alignment)
2. **RAG**
    - LLM의 제한(최신 정보 미흡, 환각 등)을 보완하기 위해 검색(외부 지식) 결합
    - Chunking & Embedding으로 문서를 나누고 효과적으로 임베딩
    - Hybrid search, Query expansion 등으로 더욱 정확한 검색
3. **Instruction Tuning**
    - 사용자와의 대화 데이터(질문-응답 쌍)로 모델을 지도학습
    - Self-Instruct, Self-alignment, WizardLM 등 다양한 합성 데이터 생성 기법
4. **Alignment Tuning**
    - 모델이 인간의 선호도, 사회적 기준을 지킬 수 있도록 RLHF나 AI-feedback 방식으로 학습
    - DPO, ULMA, Self-rewarding 등 세부 최적화 기법 존재