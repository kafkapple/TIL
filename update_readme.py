import os
import re
from datetime import datetime

def get_markdown_files(base_directory):
    """
    Find markdown files across directory hierarchy, excluding README.md
    """
    hierarchy = {}
    
    for root, dirs, files in os.walk(base_directory):
        # Skip _Daily folder and base directory
        if '_Daily' in root or root == base_directory:
            continue
        
        # Filter markdown files, excluding README.md
        md_files = [f for f in files if f.endswith('.md') and f.lower() != 'readme.md']
        
        # Skip directories with no markdown files
        if not md_files:
            continue
        
        # Relative path from base directory
        relative_path = os.path.relpath(root, base_directory)
        path_parts = [p for p in relative_path.split(os.path.sep) if p != '.']
        
        # Traverse or create hierarchy
        current = hierarchy
        for part in path_parts:
            if part not in current:
                current[part] = {}
            current = current[part]
        
        # Add markdown files to current level
        current['__files__'] = md_files
    
    return hierarchy

def parse_markdown_files(base_directory):
    """
    Parse markdown files with advanced sorting and linking
    """
    til_content = ""
    daily_files = {}
    
    # Process _Daily folder files
    daily_path = os.path.join(base_directory, '_Daily')
    
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
                'full_path': os.path.join('_Daily', filename)
            })
    
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
                # Remove .md extension from link
                link_filename = os.path.splitext(file_info['filename'])[0]
                til_content += f"- [{file_info['filename']}]({os.path.join('_Daily', link_filename)}) ({file_info['topic']})\n"
            til_content += "\n"
    
    # Process other markdown files with hierarchy
    til_content += "# 기타 문서\n\n"
    file_hierarchy = get_markdown_files(base_directory)
    
    def process_hierarchy(hierarchy, current_path='', depth=1):
        nonlocal til_content
        for key, value in sorted(hierarchy.items()):
            if key == '__files__':
                for filename in sorted(value):
                    # Remove .md extension from link
                    link_filename = os.path.splitext(filename)[0]
                    file_link_path = os.path.join(current_path, link_filename)
                    til_content += f"- [{filename}]({file_link_path})\n"
            else:
                # Create headings based on depth
                heading = '#' * (depth + 1)
                til_content += f"{heading} {key}\n\n"
                
                # Update current path for linking
                new_path = os.path.join(current_path, key) if current_path else key
                process_hierarchy(value, new_path, depth + 1)
    
    process_hierarchy(file_hierarchy)
    
    return til_content

def update_readme():
    # 작성한 내용을 README.md 파일에 저장
    til_content = parse_markdown_files('.')
    with open("./README.md", "w", encoding='utf-8') as f:
        f.write(til_content)

if __name__ == "__main__":
    update_readme()
    print("README.md has been updated.")
