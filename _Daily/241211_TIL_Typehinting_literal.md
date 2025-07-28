# Typehinting_literal

20241211_Typehinting_literal

- Literal['text', 'html', 'markdown'] 데이터 타입

- output_format 매개변수에 사용되며, 다음 세 가지 문자열 중 하나만 선택할 수 있음을 의미

```bash

from typing import Literal

def render_content(content: str, format: Literal['text', 'html', 'markdown']) -> str:

if format == 'text':

```