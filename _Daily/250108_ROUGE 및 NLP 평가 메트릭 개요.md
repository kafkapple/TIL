# 📄 ROUGE

ROUGE는 자연어 생성(NLG) 모델의 성능을 평가하기 위한 표준 지표로, 생성된 텍스트와 참조 텍스트 간의 유사도를 정량적으로 측정

### 1. ROUGE 개요

#### 1.1 기본 개념

- **ROUGE(Recall-Oriented Understudy for Gisting Evaluation)** 정의

- **목적**: 텍스트 요약, 기계 번역 등 NLG 모델 성능 평가

- **측정 방식**: 생성 텍스트와 참조 텍스트 간 유사도 정량화 (0~1 범위)

#### 1.2 평가 지표

- **Recall**: 참조 요약 내 n-그램이 생성 요약에 등장한 비율

- **Precision**: 생성 요약 내 n-그램이 참조 요약에 등장한 비율

- **F1-score**: Recall과 Precision의 조화 평균

### 2. ROUGE 종류

#### 2.1 N-gram 기반

- **ROUGE-N**: 연속된 n개 단어(n-gram) 겹침 개수 계산

- ROUGE-1: Unigram (단어 단위)

- ROUGE-2: Bigram (두 단어 단위)

- **ROUGE-S/ROUGE-SU**: Skip-bigram 또는 Unigram과 Bigram 조합 고려

#### 2.2 순서 및 연속성 기반

- **ROUGE-L**: 최장 공통 부분수열(Longest Common Subsequence, LCS) 기반 Recall 계산

- **ROUGE-W**: ROUGE-L 확장, 연속적인 매칭에 가중치 부여

### 3. ROUGE 활용

#### 3.1 적용 분야

- 텍스트 요약, 기계 번역

- 콘텐츠 생성, RAG(검색 기반 생성)

- 질의응답 시스템

#### 3.2 실제 사용

- ROUGE-1, ROUGE-2, ROUGE-L 등 여러 변형 조합하여 모델 성능 비교

- 주로 영어 평가에 사용되나, 한국어 등 다른 언어에도 적용 가능