from datetime import datetime
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

        year, month, day, topic = match.groups()
        year = f"20{year}"
        
        file_date = datetime(int(year), int(month), int(day))
        # 월별 주차 계산
        first_day = datetime(int(year), int(month), 1)
        days_diff = (file_date - first_day).days
        week_number = (days_diff // 7) + 1

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

class ReadmeGenerator:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def generate_daily_content(self):
        content = []
        for year in sorted(self.file_manager.daily_files.keys(), reverse=True):
            content.append(f"# {year}년 학습 기록\n")
            year_data = self.file_manager.daily_files[year]
            
            for month in sorted(year_data.keys(), reverse=True):
                content.append(f"## {year}년 {month}월\n")
                month_data = year_data[month]
                
                for week in sorted(month_data.keys(), reverse=True):
                    content.append(f"### {week}주차\n")
                    files = sorted(month_data[week], key=lambda x: x.date, reverse=True)
                    
                    for file in files:
                        content.append(
                            f"- [{file.topic}]({file.safe_path}) ({file.weekday})\n"
                        )
                    content.append("\n")
        
        return "".join(content)

def update_readme():
    manager = DailyFileManager('.')
    manager.collect_files()
    
    generator = ReadmeGenerator(manager)
    content = generator.generate_daily_content()
    
    with open("./README.md", "w", encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
    print("README.md has been updated.")
