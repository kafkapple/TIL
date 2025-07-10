# Path
- 파일 확장자 가져오기
    - print(path.suffix)
- Path.as_posix()를 사용하여 경로 구분자를 '/'로 통일
### **POSIX 스타일이 필요한 경우에만 `.as_posix()` 사용**
`as_posix()`는 문자열 변환이므로, 실제 작업은 여전히 `Path` 객체를 사용하도록 권장
```python
posix_path = path.as_posix()  # '/example/subdir/file.txt'
```
# Latex
\frac{분자}{분모}
$$
\frac{분자 Numerator}{분모 Denominator}
$$
### 간단한 기억법:
- **Numerator (분자)**: 위쪽 숫자 → "Number"에서 파생.
- **Denominator (분모)**: 아래쪽 숫자 → "Denote"의 어원이 포함되어 '전체를 나타내는' 의미.