import os
import re
from datetime import datetime, timedelta
from collections import defaultdict
from urllib.parse import quote

# --- 설정 ---
DAILY_DIR = "_Daily"
README_FILE = "README.md"
WEEKDAY_NAMES = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
LEVEL_SYMBOLS = ["⬜️", "🟩", "🟢", "💚", "🌳"]

class MarkdownFile:
    """TIL 파일 정보를 담는 데이터 클래스"""
    def __init__(self, filename, full_path, date, topic):
        self.filename = filename
        self.full_path = full_path
        self.date = date
        self.topic = topic

    @property
    def safe_path(self):
        return quote(self.full_path)

class ReadmeGenerator:
    """README.md 생성을 위한 모든 로직을 관리하는 클래스"""
    def __init__(self):
        self.daily_files = defaultdict(list)
        self.contributions = defaultdict(int)
        self._collect_daily_files()

    def _collect_daily_files(self):
        """_Daily 폴더를 스캔하여 파일 정보와 기여도를 수집합니다."""
        if not os.path.isdir(DAILY_DIR):
            return

        for filename in os.listdir(DAILY_DIR):
            match = re.match(r'(?:20)?(\d{2})(\d{2})(\d{2})_(.*)\.md', filename)
            if match:
                year, month, day, topic = match.groups()
                year = int(f"20{year}")
                try:
                    date = datetime(year, int(month), int(day))
                    full_path = os.path.join(DAILY_DIR, filename)
                    md_file = MarkdownFile(filename, full_path, date, topic)
                    
                    self.daily_files[year].append(md_file)
                    self.contributions[date.date()] += 1
                except ValueError:
                    continue

    def generate_heatmap_for_year(self, year):
        """특정 연도에 대한 히트맵을 생성합니다. (숫자 월, 2칸 정렬)"""
        start_of_year = datetime(year, 1, 1).date()
        end_of_year = datetime(year, 12, 31).date()
        
        start_of_first_week = start_of_year - timedelta(days=(start_of_year.weekday() + 1) % 7)
        total_weeks = (end_of_year - start_of_first_week).days // 7 + 1
        
        grid = [[-1] * total_weeks for _ in range(7)]
        month_labels = ["  "] * total_weeks

        for day_offset in range((end_of_year - start_of_year).days + 1):
            date = start_of_year + timedelta(days=day_offset)
            week_num = (date - start_of_first_week).days // 7
            weekday = (date.weekday() + 1) % 7

            if 0 <= week_num < total_weeks:
                if date.day == 1:
                    month_labels[week_num] = f"{date.month:<2}"
                
                count = self.contributions.get(date, 0)
                level = min(count, len(LEVEL_SYMBOLS) - 1) if count > 0 else 0
                grid[weekday][week_num] = level

        # 헤더(월) 문자열 생성 (2칸 단위)
        header = "    " + "".join(month_labels)
        
        # 그리드(요일) 문자열 생성 (2칸 단위)
        lines = [header]
        for i, day_name in enumerate(WEEKDAY_NAMES):
            line = f"{day_name: <3}|"
            for week in range(total_weeks):
                level = grid[i][week]
                # 이모지는 이미 2칸 너비, 빈 칸은 2칸 공백으로 처리
                line += LEVEL_SYMBOLS[level] if level != -1 else "  "
            lines.append(line + "|")
        
        return "\n".join(lines)

    def generate_all_heatmaps(self):
        """수집된 모든 연도에 대한 히트맵을 생성합니다."""
        content = ["## 🗓️ Daily Learning Log"]
        sorted_years = sorted(self.daily_files.keys(), reverse=True)

        for year in sorted_years:
            content.append(f"### {year}")
            heatmap_str = self.generate_heatmap_for_year(year)
            content.append(f"```\n{heatmap_str}\n```")
        
        legend = "Less ⬜️ 🟩 🟢 💚 🌳 More"
        content.append(f"<div align=\"right\">{legend}</div>\n")
        return "\n".join(content)

    def generate_daily_log(self):
        """연/월/주 단위의 학습 로그를 생성합니다."""
        content = ["## 📚 Learning Archive"]
        sorted_years = sorted(self.daily_files.keys(), reverse=True)

        for year in sorted_years:
            content.append(f"### {year}")
            
            monthly_files = defaultdict(lambda: defaultdict(list))
            for md_file in self.daily_files[year]:
                # 월의 첫 날을 기준으로 주차 계산
                first_day_of_month = md_file.date.replace(day=1)
                # 첫 날의 요일 (일요일=0, 월요일=1, ...)
                first_weekday = (first_day_of_month.weekday() + 1) % 7
                # 주차 계산
                week_num = (md_file.date.day + first_weekday - 1) // 7 + 1
                monthly_files[md_file.date.month][week_num].append(md_file)
            
            for month in sorted(monthly_files.keys(), reverse=True):
                month_name = datetime(year, month, 1).strftime("%B")
                content.append(f"- #### {month_name}")
                for week in sorted(monthly_files[month].keys()):
                    content.append(f"  - **Week {week}**")
                    for md_file in sorted(monthly_files[month][week], key=lambda f: f.date):
                        date_str = md_file.date.strftime("%d, %a")
                        content.append(f"    - [{md_file.topic}]({md_file.safe_path}) - *{date_str}*")
        return "\n".join(content)

    def write_readme(self):
        """모든 콘텐츠를 조합하여 README.md 파일을 작성합니다."""
        print("-> README.md 생성 시작...")
        content = [
            "# TIL Dashboard",
            self.generate_all_heatmaps(),
            self.generate_daily_log(),
        ]
        
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
        print("   README.md가 성공적으로 업데이트되었습니다.")

def update_readme():
    generator = ReadmeGenerator()
    generator.write_readme()

if __name__ == "__main__":
    update_readme()
