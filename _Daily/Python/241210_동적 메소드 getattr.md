### `getattr`을 활용한 동적 메서드 호출

### 1. **기능**

- `getattr`: 문자열로 객체의 속성(메서드 포함)을 동적으로 호출하는 Python 함수.

---

### 2. **용법**

- **기본 구조**
    
    ```python
    getattr(객체, "속성명(문자열)", [기본값])
    ```
    
    - 첫 번째 인자: 호출 대상 객체.
    - 두 번째 인자: 속성명(메서드나 변수 이름).
    - 세 번째 인자(선택): 속성이 없을 때 반환할 기본값.
- **예제 1: 동적 메서드 호출**
    
    ```python
    
    class Calculator:
        def add(self, a, b):
            return a + b
    
    calc = Calculator()
    method = getattr(calc, "add")  # 'add' 메서드 가져오기
    print(method(5, 3))  # 출력: 8
    ```
    
- **예제 2: 기본값 설정**
    
    ```python
    
    result = getattr(calc, "multiply", lambda a, b: "Not implemented")(5, 3)
    print(result)  # 출력: Not implemented
    
    ```
    

---

**응용: 플러그인 시스템**

```python

class Plugin:
    def greet(self, name):
        return f"Hello, {name}!"

def execute_action(plugin, action, *args):
    method = getattr(plugin, action, lambda *args: "Action not available")
    return method(*args)

plugin = Plugin()
print(execute_action(plugin, "greet", "Alice"))  # 출력: Hello, Alice!
print(execute_action(plugin, "unknown", "Alice"))  # 출력: Action not available
```

### 3. **장점**

- **유연성**: 플러그인 메커니즘, 동적 API 설계, 동적 명령 실행에 유용.
- **확장성**: 정적 코딩 없이 기능 확장 가능.

### 4. **단점**

- **런타임 오류 위험**: 잘못된 속성명 사용 시 예외 발생.
- **가독성 저하**: 코드 추적이 어려워질 수 있음.

---

### 5. **추천**

- 고정된 속성 호출 시에는 명시적으로 호출.
- 동적 로직에 필수적인 경우 `getattr`을 사용하되:
    - 기본값 설정으로 예외 처리.
    - 주석과 문서화를 통해 가독성 유지.