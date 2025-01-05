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
