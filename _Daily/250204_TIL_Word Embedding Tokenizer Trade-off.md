# 📄 Word Embedding Tokenizer Trade-off

Word-level과 Character-level 임베딩 방식의 장단점 및 서브워드 토크나이징의 필요성 이해.

### 1. Word-Level Embedding

#### 1.1 개념 및 특징

- 핵심 개념(Key Term) 정의: 각 단어에 고유한 임베딩 벡터 할당.

- 이론적 원리 이해: 단어의 의미를 문맥 기반으로 직접 표현.

- 수식/구조 정리: Word2Vec, GloVe 등 전통적 방식.

#### 1.2 장점 및 한계

- 장점: 문맥 유지, 직관적 의미 표현.

- 단점: Vocabulary Size 증가, 희소성(Sparsity) 문제, OOV(Out-Of-Vocabulary) 단어 처리 불가.

### 2. Character-Level Embedding

#### 2.1 개념 및 특징

- 핵심 개념(Key Term) 정의: 단어를 문자 단위로 분해하여 각 문자에 임베딩 벡터 할당.

- 이론적 원리 이해: 문자를 조합하여 단어 의미 학습 시도.

- 수식/구조 정리: CNN/RNN 기반 모델, BERT 일부 변형 활용.

#### 2.2 장점 및 한계

- 장점: Vocabulary Size 대폭 축소, OOV 문제 해결.

- 단점: 단어 의미 학습 어려움, 긴 문장에서 Token 수 과다 증가, 계산량 증가.

### 3. Trade-off 및 해결책

#### 3.1 Word-Level vs Character-Level Trade-off

- Word-Level: 단어 수 증가로 인한 희소성 및 OOV 문제.

- Character-Level: Token 수 증가로 인한 계산량 및 의미 학습 어려움.

#### 3.2 Subword Tokenizing

- 핵심 개념(Key Term) 정의: 단어를 의미 있는 서브워드 단위로 분할.

- 이론적 원리 이해: Word-level과 Character-level의 단점 절충.

- 수식/구조 정리: BPE, WordPiece, SentencePiece 등.