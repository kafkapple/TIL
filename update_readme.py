import os
import re
from datetime import datetime

def parse_markdown_files(base_directory):
    """
    Parse markdown files with advanced sorting logic
    
    Args:
        base_directory (str): Base directory containing markdown files
    
    Returns:
        str: Parsed markdown content for README
    """
    til_content = ""
    daily_files = {}
    other_files = {}
    
    # Separate Daily folder and other markdown files
    daily_path = os.path.join(base_directory, '_Daily')
    
    # Process Daily folder files
    for filename in os.listdir(daily_path):
        match = re.match(r'(\d{4})(\d{2})(\d{2})_(\w+)\.md', filename)
        
        if match:
            year, month, day, topic = match.groups()
            
            # Create datetime for sorting
            file_date = datetime(int(year), int(month), int(day))
            
            if year not in daily_files:
                daily_files[year] = {}
            
            if month not in daily_files[year]:
                daily_files[year][month] = []
            
            daily_files[year][month].append({
                'filename': filename,
                'topic': topic,
                'date': file_date,
                'full_path': os.path.join(daily_path, filename)
            })
    
    # Process other markdown files in base directory
    for filename in os.listdir(base_directory):
        if filename.endswith('.md') and not filename.startswith('README') and not os.path.isdir(os.path.join(base_directory, filename)):
            category = filename.split('_')[0] if '_' in filename else 'Uncategorized'
            
            if category not in other_files:
                other_files[category] = []
            
            other_files[category].append(filename)
    
    # Generate README content for Daily files
    for year in sorted(daily_files.keys(), reverse=True):
        til_content += f"# {year}년 학습 기록\n\n"
        for month in sorted(daily_files[year].keys(), reverse=True):
            til_content += f"## {year}년 {month}월\n\n"
            
            # Sort files by date in descending order
            sorted_files = sorted(
                daily_files[year][month], 
                key=lambda x: x['date'], 
                reverse=True
            )
            
            for file_info in sorted_files:
                til_content += f"- {file_info['filename']} ({file_info['topic']})\n"
            til_content += "\n"
    
    # Add other markdown files, sorted alphabetically
    til_content += "# 기타 문서\n\n"
    for category, files in sorted(other_files.items()):
        til_content += f"## {category}\n\n"
        for filename in sorted(files):
            til_content += f"- {filename}\n"
        til_content += "\n"
    
    return til_content

def update_readme():
    # 작성한 내용을 README.md 파일에 저장
    til_content = parse_markdown_files('.')
    with open("./README.md", "w", encoding='utf-8') as f:
        f.write(til_content)

if __name__ == "__main__":
    update_readme()
    print("README.md has been updated.")
