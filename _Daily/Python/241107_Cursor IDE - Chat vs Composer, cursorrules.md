## Cursor IDE의 Chat과 Composer의 주요 차이
### Chat
- 일반적인 AI 채팅 인터페이스
- 코드에 대한 질문/답변, 설명 요청, 디버깅 도움 등 자유로운 대화 형식
- 실시간으로 현재 작업 중인 코드 컨텍스트를 이해하고 응답
- 빠른 피드백과 상호작용에 적합
### Composer
- 대규모 코드 생성과 리팩토링에 특화
- 여러 파일을 동시에 수정하거나 새로운 기능을 구현할 때 유용
- 프로젝트 구조를 이해하고 일관된 코드 스타일 유지
- 더 구조화된 작업 흐름 제공
- Git 커밋 메시지 자동 생성 기능 포함
예시 사용 상황:
- Chat: "이 에러 메시지가 무슨 뜻인가요?", "이 함수를 어떻게 개선할 수 있을까요?"
- Composer: "새로운 API 엔드포인트와 관련 테스트 코드를 생성해주세요", "이 모듈을 리팩토링해주세요"
# Cursorrules
- 해당 프로젝트 루트에 .cursorrules 파일
    - prompt