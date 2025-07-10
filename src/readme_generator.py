import os
import re
from datetime import datetime, timedelta
from collections import defaultdict
from urllib.parse import quote

# --- 설정 ---
DAILY_DIR = "_Daily"
README_FILE = "README.md"
MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
WEEKDAY_NAMES = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
LEVEL_SYMBOLS = ["⬜️", "🟩", "🟢", "💚", "🌳"]

def get_til_contributions():
    """_Daily 폴더를 스캔하여 날짜별 TIL 작성 횟수를 반환합니다."""
    contributions = defaultdict(int)
    if not os.path.isdir(DAILY_DIR):
        return contributions

    for filename in os.listdir(DAILY_DIR):
        match = re.match(r'(?:20)?(\d{2})(\d{2})(\d{2})_.*\.md', filename)
        if match:
            year, month, day = [int(g) for g in match.groups()]
            # Y2K 이후 날짜 처리
            year += 2000 if year < 100 else 0
            try:
                date = datetime(year, month, day)
                contributions[date.date()] += 1
            except ValueError:
                continue # 유효하지 않은 날짜는 건너뜁니다.
    return contributions

def generate_heatmap(contributions):
    """지난 1년간의 기여도를 바탕으로 텍스트 기반 히트맵을 생성합니다."""
    today = datetime.now().date()
    end_date = today
    start_date = end_date - timedelta(days=365)

    # 53주 x 7일 그리드 생성 (초기값: -1, 빈 칸 의미)
    grid = [[-1] * 53 for _ in range(7)]
    
    # 월별 레이블 위치 계산
    month_labels = [""] * 53

    current_date = start_date
    while current_date <= end_date:
        # ISO 달력 기준: 월요일(0) ~ 일요일(6)
        iso_year, iso_week, iso_weekday = current_date.isocalendar()
        # 그리드 인덱스: 일요일(0) ~ 토요일(6)
        weekday = (iso_weekday) % 7 

        # 현재 날짜와 시작 날짜 사이의 주차 차이 계산
        week_num = (current_date - start_date).days // 7

        if 0 <= week_num < 53:
            count = contributions.get(current_date, 0)
            level = min(count, len(LEVEL_SYMBOLS) - 1)
            grid[weekday][week_num] = level

            # 매월 1일에 월 이름 기록
            if current_date.day == 1:
                month_labels[week_num] = MONTH_NAMES[current_date.month - 1]

        current_date += timedelta(days=1)

    # 히트맵 문자열 생성
    heatmap_str = "         " + " ".join(f"{label:<4}" for label in month_labels if label) + "\n"
    for i, day_name in enumerate(WEEKDAY_NAMES):
        line = f"{day_name: <3} | "
        for week in range(53):
            level = grid[i][week]
            line += LEVEL_SYMBOLS[level] if level != -1 else "  "
        heatmap_str += line + " |\n"
        
    return f"```\n{heatmap_str}```"

def get_topic_structure():
    """TIL 폴더 구조를 재귀적으로 탐색하여 목차를 생성합니다."""
    structure = {}
    for root, dirs, files in os.walk("."):
        # 특정 폴더 제외
        if any(d in root for d in [DAILY_DIR, ".git", ".github"]):
            continue

        # 마크다운 파일만 필터링
        md_files = sorted([f for f in files if f.endswith('.md')])
        if not md_files:
            continue

        # 경로를 기반으로 계층 구조 생성
        parts = root.split(os.sep)[1:] # 현재 디렉토리(.) 제외
        current_level = structure
        for part in parts:
            current_level = current_level.setdefault(part, {})
        
        current_level["_files"] = md_files

    return structure

def generate_topic_content(structure, level=0):
    """재귀적으로 목차 내용을 생성합니다."""
    content = []
    indent = "  " * level
    for key, value in sorted(structure.items()):
        if key == "_files":
            for file in value:
                topic = os.path.splitext(file)[0]
                path = os.path.join(key, file)
                # URL 인코딩 적용
                safe_path = quote(path)
                content.append(f"{indent}- [{topic}]({safe_path})\n")
        else:
            content.append(f"{indent}## {key}\n")
            content.append(generate_topic_content(value, level + 1))
    return "".join(content)

def update_readme():
    """README.md 파일을 생성하고 업데이트합니다."""
    print("README 업데이트 시작...")
    
    # 1. TIL 기여도 데이터 수집 및 히트맵 생성
    contributions = get_til_contributions()
    heatmap = generate_heatmap(contributions)
    print("히트맵 생성 완료.")

    # 2. 토픽 목차 생성
    topic_structure = get_topic_structure()
    topic_content = generate_topic_content(topic_structure)
    print("토픽 목차 생성 완료.")

    # 3. README 내용 조합
    readme_content = f"# TIL Dashboard\n\n## Contribution Heatmap\n{heatmap}\n\n# Topics\n{topic_content}"

    # 4. 파일 쓰기
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print(f"'{README_FILE}' 파일이 성공적으로 업데이트되었습니다.")

if __name__ == "__main__":
    update_readme()