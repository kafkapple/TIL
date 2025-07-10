from datetime import datetime, timedelta
import os
import re
from urllib.parse import quote

class MarkdownFile:
    def __init__(self, filename, full_path, date, topic):
        self.filename = filename
        self.full_path = full_path
        self.date = date
        self.weekday = date.strftime('%a')
        self.topic = topic
        
    @property
    def safe_path(self):
        """URL-safe 경로 반환"""
        return quote(self.full_path)

class DailyFileManager:
    def __init__(self, base_directory):
        self.base_directory = base_directory
        self.daily_files = {}

    def process_file(self, root, filename):
        if not filename.endswith('.md'):
            return

        match = re.match(r'(?:20)?(\d{2})(\d{2})(\d{2})_(.+)\.md', filename)
        if not match:
            return

        year, month, day = match.groups()[:3]
        topic = match.groups()[3]
        year = f"20{year}"
        
        file_date = datetime(int(year), int(month), int(day))
        
        # 월요일 기준 주차 계산
        first_day = datetime(int(year), int(month), 1)
        
        # 해당 월의 첫 월요일 찾기
        while first_day.weekday() != 0:  # 0은 월요일
            first_day = first_day - timedelta(days=1)
            
        # 첫 월요일부터의 차이로 주차 계산
        days_diff = (file_date - first_day).days
        week_number = (days_diff // 7) + 1
        
        # 이전 달의 마지막 주에 속하는 경우 처리
        if file_date < datetime(int(year), int(month), 1):
            week_number = 0  # 이전 달의 마지막 주

        self._add_file_to_structure(
            MarkdownFile(
                filename=filename,
                full_path=os.path.relpath(os.path.join(root, filename), self.base_directory),
                date=file_date,
                topic=topic
            ),
            year, month, week_number
        )

    def _add_file_to_structure(self, md_file, year, month, week):
        self.daily_files.setdefault(year, {})
        self.daily_files[year].setdefault(month, {})
        self.daily_files[year][month].setdefault(week, [])
        self.daily_files[year][month][week].append(md_file)

    def collect_files(self):
        daily_path = os.path.join(self.base_directory, '_Daily')
        for root, _, files in os.walk(daily_path):
            for filename in files:
                self.process_file(root, filename)

class TopicFile:
    def __init__(self, filename, full_path):
        self.filename = filename
        self.full_path = full_path
        self.topic = os.path.splitext(filename)[0]
        
    @property
    def safe_path(self):
        """URL-safe 경로 반환"""
        return quote(self.full_path)

class TopicFileManager:
    def __init__(self, base_directory):
        self.base_directory = base_directory
        self.topic_structure = {}

    def collect_files(self):
        for root, dirs, files in os.walk(self.base_directory):
            print(f"Scanning directory: {root}")
            
            # 경로 부분을 개별적으로 체크
            path_parts = root.split(os.sep)
            
            # _Daily 폴더 스킵
            if '_Daily' in path_parts:
                print(f"Skipping _Daily folder: {root}")
                continue
                
            # 실제 숨김 폴더만 스킵 (폴더명이 .으로 시작하는 경우만)
            if any(part.startswith('.') and part != '.' for part in path_parts):
                print(f"Skipping hidden folder: {root}")
                continue

            relative_path = os.path.relpath(root, self.base_directory)
            if relative_path == '.':
                continue

            # 마크다운 파일 찾기
            md_files = [f for f in files if f.endswith('.md')]
            if md_files:
                print(f"Found MD files in {relative_path}: {md_files}")
                
                # 경로 파싱
                path_parts = relative_path.split(os.sep)
                current_level = self.topic_structure
                
                # 마지막 부분을 제외한 경로 처리
                for part in path_parts:
                    if part != '.':  # 현재 디렉토리 표시 무시
                        if part not in current_level:
                            current_level[part] = {}
                        current_level = current_level[part]
                
                # 현재 디렉토리의 파일들 저장
                if md_files:
                    current_level['files'] = [
                        TopicFile(
                            filename=f,
                            full_path=os.path.relpath(os.path.join(root, f), self.base_directory)
                        ) for f in md_files
                    ]

    def print_structure(self):
        """디버깅용: 수집된 구조 출력"""
        def _print_level(structure, level=0):
            indent = "  " * level
            for key, value in structure.items():
                if key == 'files':
                    print(f"{indent}Files: {[f.filename for f in value]}")
                else:
                    print(f"{indent}{key}:")
                    _print_level(value, level + 1)
        
        _print_level(self.topic_structure)

class ReadmeGenerator:
    def __init__(self, daily_manager, topic_manager):
        self.daily_manager = daily_manager
        self.topic_manager = topic_manager

    def generate_content(self):
        content = []
        
        # Daily 섹션 생성
        content.append(self.generate_daily_content())
        
        # Topics 섹션 생성
        content.append("\n# Topics\n")
        content.append(self.generate_topic_content(self.topic_manager.topic_structure))
        
        return "".join(content)

    def generate_daily_content(self):
        content = []
        for year in sorted(self.daily_manager.daily_files.keys(), reverse=True):
            content.append(f"# {year} TIL\n")
            year_data = self.daily_manager.daily_files[year]
            
            for month in sorted(year_data.keys(), reverse=True):
                content.append(f"## {year}.{month}\n")
                month_data = year_data[month]
                
                for week in sorted(month_data.keys(), reverse=True):
                    content.append(f"### Week-{week}\n")
                    files = sorted(month_data[week], key=lambda x: x.date, reverse=True)
                    
                    for file in files:
                        # 날짜 형식 추가 (월.일)
                        date_str = file.date.strftime('%m.%d')
                        content.append(
                            f"- [{file.topic}]({file.safe_path}) ({file.weekday} {date_str})\n"
                        )
                    content.append("\n")
        
        return "".join(content)

    def generate_heatmap_content(self):
        # SVG 설정
        CELL_SIZE = 12
        CELL_SPACING = 3
        WEEKDAY_LABEL_WIDTH = 40
        MONTH_LABEL_HEIGHT = 20
        
        # 요일 레이블 (월요일부터 시작)
        WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        # 색상 (활동량에 따라)
        # COLORS = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"] # GitHub-like green
        COLORS = ["#ebedf0", "#c6e48b", "#7bc96d", "#239a3b", "#196127"] # Slightly different green
        
        # TIL 날짜 데이터 준비
        til_dates = defaultdict(int) # (year, month, day) -> count
        for year_str, months in self.daily_manager.daily_files.items():
            for month_str, weeks in months.items():
                for week_num, files in weeks.items():
                    for file in files:
                        til_dates[(file.date.year, file.date.month, file.date.day)] += 1

        today = datetime.now()
        # 지난 12개월을 기준으로 히트맵 생성
        start_date = (today - timedelta(days=365)).replace(day=1)
        
        # SVG 시작
        svg_elements = []
        
        # 요일 레이블 추가
        for i, weekday in enumerate(WEEKDAYS):
            svg_elements.append(f'''<text x="0" y="{MONTH_LABEL_HEIGHT + (i * (CELL_SIZE + CELL_SPACING)) + (CELL_SIZE / 2) + 4}" class="w-label">{weekday}</text>''')

        current_x = WEEKDAY_LABEL_WIDTH
        
        # 월별 데이터 처리
        for month_offset in range(12):
            current_month_date = datetime(start_date.year, start_date.month, 1) + timedelta(days=30 * month_offset) # 대략적인 월 이동
            
            # 정확한 월 계산
            year = start_date.year + (start_date.month + month_offset - 1) // 12
            month = (start_date.month + month_offset - 1) % 12 + 1
            
            # 현재 월의 첫 날
            first_day_of_month = datetime(year, month, 1)
            
            # 월 레이블 추가
            svg_elements.append(f'''<text x="{current_x + (CELL_SIZE + CELL_SPACING) * (first_day_of_month.weekday() if first_day_of_month.weekday() != 0 else 7) / 2}" y="15" class="m-label">{calendar.month_abbr[month]}</text>''')
            
            # 해당 월의 모든 날짜 순회
            for day in range(1, calendar.monthrange(year, month)[1] + 1):
                current_date = datetime(year, month, day)
                
                # 월요일(0)부터 일요일(6)까지 매핑
                # Python의 weekday()는 월=0, 일=6
                # SVG 히트맵은 보통 일=0, 토=6 또는 월=0, 일=6
                # 여기서는 월=0, 일=6으로 사용
                day_of_week = current_date.weekday() # 0=월, 6=일
                
                # x, y 좌표 계산
                # x는 월의 시작 위치 + (요일 * 셀 크기)
                # y는 요일 * (셀 크기 + 간격)
                
                # 월의 첫 날이 시작하는 열을 기준으로 x 오프셋 계산
                # 첫 날이 월요일(0)이면 0열, 화요일(1)이면 1열... 일요일(6)이면 6열
                # 히트맵은 월요일부터 시작하므로, 월요일이 0번째 줄
                # 따라서 day_of_week를 그대로 y 좌표로 사용
                
                # 월별로 열을 계산해야 함.
                # 각 월은 새로운 열에서 시작
                # 월의 첫 날이 무슨 요일인지에 따라 첫 번째 셀의 위치가 결정됨
                
                # 이 부분은 좀 더 복잡하게 계산해야 함.
                # 전체 캘린더를 52주(대략)로 보고 각 주를 열로 표현해야 함.
                # GitHub 잔디밭처럼 주 단위로 열이 증가하는 방식
                
                # 다시 계산: 각 날짜는 해당 연도의 몇 번째 주인지, 그리고 무슨 요일인지로 위치 결정
                # 1년 52주를 기준으로 x축을 잡고, 요일을 y축으로 잡는 방식
                
                # 모든 TIL 날짜를 (년, 월, 일) 튜플로 변환
                all_til_dates = set()
                for year_str, months in self.daily_manager.daily_files.items():
                    for month_str, weeks in months.items():
                        for week_num, files in weeks.items():
                            for file in files:
                                all_til_dates.add((file.date.year, file.date.month, file.date.day))

                # 현재 연도 기준
                current_year = today.year
                
                # 히트맵 데이터 구조 초기화 (요일 x 주차)
                # 7일 * 53주 (최대)
                heatmap_data = defaultdict(lambda: defaultdict(int)) # heatmap_data[weekday][week_of_year] = count
                
                # 모든 날짜를 순회하며 데이터 채우기
                # 1월 1일부터 12월 31일까지
                for day_num in range(366): # 윤년 고려 최대 366일
                    date_to_check = datetime(current_year, 1, 1) + timedelta(days=day_num)
                    if date_to_check.year != current_year: # 다음 해로 넘어갔으면 중단
                        break
                    
                    # Python의 weekday()는 월=0, 일=6
                    # 히트맵은 월요일부터 시작하는 것이 일반적이므로 그대로 사용
                    day_of_week_idx = date_to_check.weekday() # 0:월, 1:화, ..., 6:일
                    
                    # 해당 연도의 몇 번째 주인지 계산 (ISO 주차 기준)
                    # ISO 주차는 월요일을 주의 시작으로 간주
                    week_of_year = date_to_check.isocalendar()[1]
                    
                    if (date_to_check.year, date_to_check.month, date_to_check.day) in all_til_dates:
                        heatmap_data[day_of_week_idx][week_of_year] += 1 # TIL이 있으면 카운트 증가

                # SVG 그리기
                # x축은 주차, y축은 요일
                
                # 최대 주차 찾기 (SVG 너비 계산용)
                max_week = 0
                for weekday_data in heatmap_data.values():
                    if weekday_data:
                        max_week = max(max_week, max(weekday_data.keys()))
                
                # SVG 너비 계산
                SVG_WIDTH = WEEKDAY_LABEL_WIDTH + (max_week + 1) * (CELL_SIZE + CELL_SPACING) + 10 # +10은 여백
                SVG_HEIGHT = MONTH_LABEL_HEIGHT + 7 * (CELL_SIZE + CELL_SPACING) + 10 # +10은 여백

                svg_elements = []
                
                # 스타일 정��
                svg_elements.append('''<style>
.w-label { font: 9px sans-serif; fill: #586069; }
.m-label { font: 9px sans-serif; fill: #586069; }
.day-cell { stroke: rgba(27,31,35,0.06); stroke-width: 1px; }
</style>''')

                # 요일 레이블 (월요일부터 일요일)
                for i, weekday_label in enumerate(WEEKDAYS):
                    svg_elements.append(f'''<text x="0" y="{MONTH_LABEL_HEIGHT + (i * (CELL_SIZE + CELL_SPACING)) + (CELL_SIZE / 2) + 4}" class="w-label">{weekday_label}</text>''')

                # 월 레이블 (대략적인 위치)
                # 각 월의 첫 번째 날짜가 속하는 주의 x 위치를 기준으로 월 레이블을 배치
                month_starts_x = defaultdict(int)
                for day_num in range(366):
                    date_to_check = datetime(current_year, 1, 1) + timedelta(days=day_num)
                    if date_to_check.year != current_year:
                        break
                    
                    week_of_year = date_to_check.isocalendar()[1]
                    
                    # 해당 월의 첫 날이 속하는 주의 x 위치를 저장
                    if date_to_check.day == 1:
                        month_starts_x[date_to_check.month] = WEEKDAY_LABEL_WIDTH + (week_of_year - 1) * (CELL_SIZE + CELL_SPACING)

                for month_idx in range(1, 13):
                    if month_idx in month_starts_x:
                        svg_elements.append(f'''<text x="{month_starts_x[month_idx]}" y="15" class="m-label">{calendar.month_abbr[month_idx]}</text>''')

                # 날짜 셀 그리기
                for day_num in range(366):
                    date_to_check = datetime(current_year, 1, 1) + timedelta(days=day_num)
                    if date_to_check.year != current_year:
                        break
                    
                    day_of_week_idx = date_to_check.weekday() # 0:월, 6:일
                    week_of_year = date_to_check.isocalendar()[1]
                    
                    # x, y 좌표 계산
                    x = WEEKDAY_LABEL_WIDTH + (week_of_year - 1) * (CELL_SIZE + CELL_SPACING)
                    y = MONTH_LABEL_HEIGHT + day_of_week_idx * (CELL_SIZE + CELL_SPACING)
                    
                    # TIL 존재 여부에 따른 색상 결정
                    count = til_dates[(date_to_check.year, date_to_check.month, date_to_check.day)]
                    color_idx = min(count, len(COLORS) - 1) # 활동량에 따라 색상 인덱스 결정
                    fill_color = COLORS[color_idx]
                    
                    svg_elements.append(f'''<rect x="{x}" y="{y}" width="{CELL_SIZE}" height="{CELL_SIZE}" fill="{fill_color}" class="day-cell" data-date="{date_to_check.strftime('%Y-%m-%d')}" data-count="{count}"></rect>''')

                # SVG 최종 조립
                svg_content = f'''<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" xmlns="http://www.w3.org/2000/svg">
{ "".join(svg_elements) }
</svg>'''
                
                return f"<!-- TIL_HEATMAP_START -->\n{svg_content}\n<!-- TIL_HEATMAP_END -->\n\n"

    def generate_topic_content(self, structure, level=0):
        content = []
        
        for key, value in sorted(structure.items()):
            indent = "  " * level
            if key == 'files':
                # 파일 목록 처리
                for file in sorted(value, key=lambda x: x.filename):
                    content.append(f"{indent}- [{file.topic}]({file.safe_path})\n")
            else:
                # 디렉토리 처리
                content.append(f"{indent}## {key}\n")
                content.append(self.generate_topic_content(value, level + 1))
        
        return "".join(content)

def update_readme():
    daily_manager = DailyFileManager('.')
    daily_manager.collect_files()
    
    topic_manager = TopicFileManager('.')
    topic_manager.collect_files()
    
    # 디버깅을 위한 구조 출력
    print("\nCollected Topic Structure:")
    topic_manager.print_structure()
    
    generator = ReadmeGenerator(daily_manager, topic_manager)
    content = generator.generate_content()
    
    with open("./README.md", "w", encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
    print("README.md has been updated.")
