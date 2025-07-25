# Seminar - Neuroscience: Causal Evidence of a Line Attractor Encoding an Affective State
### 주요 내용
1. **Line Attractor와 감정 상태의 코딩**
    - Anderson Lab은 aggression과 arousal 같은 감정 상태가 **line attractor dynamics**로 코딩된다는 연구를 발표해왔으며, 이번 연구에서는 이를 **causal evidence**로 확장.
    - 연구 방법:
        - 2-photon imaging
        - Holographic optogenetic stimulation
        - Computational modeling
    - 주요 발견:
        - **Line attractor**를 형성하는 뉴런들의 **causal role** 규명.
        - 해당 neuronal ensemble의 **synaptic properties**가 attractor stability에 미치는 영향 분석.
2. **Population Vector의 역할**
    - 뉴런의 population activity를 분석하여 density와 energy landscape로 변환.
    - **Low-level energy state → attractor 안정성 제공.**
3. **Neuron Subtypes (x1, x2)의 특성: SLDS 를 통해 time-series data 를 discrete 분석**
    - **x1 뉴런**: 지속적인 활동(sustained activity)을 보여 line attractor에 수렴.
        - Time constant가 크며 emotion stability와 관련 있음.
    - **x2 뉴런**: Transient activity를 보이며 즉각적이고 빠른 반응 담당.
        - Stimulus 종료 후 baseline으로 빠르게 복귀.
    - 두 뉴런은 activity autocorrelation 분석에서 상이한 패턴을 보여줌.
4. **Line Attractor의 Synaptic 및 Network 특성**
    - Emotion stability는 slow neurotransmission time constant(GPCR)와 network density에 의해 영향을 받음.
    - **Network density**가 너무 높으면 feedback loop로 인해 instability 발생 가능.
---
### 논의 및 비판
1. **Population-Level Dynamics의 타당성**
    - **김민유**:
        - Line attractor를 population level로 보는 해석이 타당한가?
            - single unit 에서도 충분히 나오는 특성을?
        - Integrator와 attractor의 경계가 명확하지 않으며, 이는 neuronal subtype에 따른 자연스러운 구분일 수 있음.
2. **Neuron Subtypes (x1, x2) 해석의 한계**
    - **x1 뉴런**: 지속적인 aggression(에스트로겐에 의한)과 관련.
    - **x2 뉴런**: 즉각적이고 일시적인 반응 담당.
    - 연구 해석이 overly deterministic
3. **Integrators vs Attractors**
    - leaky integrator = **Line attractor** 로 해석했으나, 이는 단순히 신경전달물질(glutamate vs neuropeptide) 특성의 차이를 fancy하게 표현한 것일 수 있음.
    - Integrator는 외부 perturbation의 영향을 받는 반면 attractor는 안정적인 차이
        - 모델링의 설계 의도에 따라 차이가 발생할 수?
4. **VMH 세부 부위 구분에 대한 의문**
    - VMH의 부위를 지나치게 세분화하여 결과를 해석하고 있음.
    - 후속 연구(bioRxiv 논문) 발표를 위한 기반 작업일 가능성.
5. **Line Attractor의 Task Dependency**
    - Line attractor의 형성이 random signal input으로도 발생 가능한 구조인가?
    - Task-dependent한 attractor가 존재하며, 특정 행동(task)에 따라 point attractor로 나뉠 가능성.
---
### 질문 및 추가 논의
1. **Individuality 및 Behavior Correlate**
    - 개인차(individual differences)는 line attractor 형성과 어떤 연관이 있는가?
    - 사회적 요인(social factors), 예를 들어 계급(hierarchy)이나 환경적 변수는 attractor 안정성에 영향을 미치는가?
2. **x1과 x2의 기능적 차이**
    - x1 뉴런이 감정의 지속성과 관련되고, x2 뉴런이 즉각적인 행동 반응과 관련된다는 해석이 설득력이 있는가?
    - 이 두 뉴런의 상호작용이 감정 상태의 전환이나 유지에 어떻게 기여하는가?
3. **Network Density와 Stability**
    - Network density가 attractor 안정성에 미치는 영향은 과장된 해석인가?
    - 적정 density 수준을 유지하지 못할 경우 instability가 발생하는 기전은?
4. **모델의 일반화 가능성**
    - Line attractor는 특정 task-dependent 구조인가, 아니면 뉴런 네트워크의 일반적 특성인가?
    - 연구 결과를 다른 감정 상태나 행동 모델에 적용할 수 있는지?