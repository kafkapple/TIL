import os
import shutil
import subprocess
import datetime

# --- 설정 (사용자 환경에 맞게 수정) ---

# 여러 컴퓨터 환경을 위한 경로 목록
# 각 항목은 (Obsidian TIL 폴더, GitHub TIL 폴더)의 쌍으로 구성
POSSIBLE_PATHS = [
    # 예시: Joon의 Linux 데스크탑
    (
        "/home/joon/Documents/Obsidian/10_Areas/TIL",
        "/home/joon/dev/TIL"
    ),
    # 예시: Joon의 Macbook
    (
        "/Users/joon/Documents/Obsidian/10_Areas/TIL",
        "/Users/joon/dev/TIL"
    ),
    # 예시: 다른 컴퓨터
    (
        "D:/Documents/Obsidian/10_Areas/TIL",
        "D:/dev/TIL"
    ),
]

COMMIT_MESSAGE = f"TIL Sync: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# --- 스크립트 본체 ---

def find_paths():
    """설정된 경로 목록에서 현재 환경에 맞는 실제 경로를 찾습니다."""
    for source_path, target_path in POSSIBLE_PATHS:
        if os.path.isdir(source_path) and os.path.isdir(target_path):
            print(f"경로 발견:")
            print(f"  - 소스 (Obsidian): {source_path}")
            print(f"  - 타겟 (GitHub): {target_path}")
            return source_path, target_path
    print("오류: 현재 환경에 맞는 소스 또는 타겟 경로를 찾을 수 없습니다.")
    print("POSSIBLE_PATHS 변수를 확인해주세요.")
    return None, None

def sync_files(source_dir, target_dir):
    """소스 디렉토리의 모든 내용을 타겟 디렉토리로 복사합니다."""
    print(f"\n[1/4] 파일 동기화 시작...")
    try:
        # .git 폴더는 제외하고 모든 파일/디렉토리를 복사
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            target_item = os.path.join(target_dir, item)

            if item == '.git':
                continue
            
            if os.path.isdir(source_item):
                shutil.copytree(source_item, target_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, target_item)
        print("파일 동기화 완료.")
        return True
    except Exception as e:
        print(f"오류: 파일 동기화 중 예외 발생 - {e}")
        return False

def run_command(command, working_dir):
    """지정된 디렉토리에서 명령어를 실행하고 결과를 출력합니다."""
    print(f"  > 실행: {' '.join(command)}")
    try:
        result = subprocess.run(
            command,
            cwd=working_dir,
            check=True,
            text=True,
            capture_output=True
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"오류: 명령어 실행 실패 (종료 코드: {e.returncode})")
        print(e.stdout)
        print(e.stderr)
        return False
    except FileNotFoundError:
        print(f"오류: '{command[0]}' 명령을 찾을 수 없습니다. 시스템에 설치되어 있는지 확인하세요.")
        return False

def get_current_branch(working_dir):
    """현재 Git 브랜치 이름을 가져옵니다."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=working_dir,
            check=True,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception:
        return None

def main():
    """메인 동기화 로직을 실행합니다."""
    source_dir, target_dir = find_paths()
    if not source_dir:
        return

    if not sync_files(source_dir, target_dir):
        return

    print("\n[2/4] README 업데이트 스크립트 실행...")
    if not run_command(["python", "update_readme.py"], target_dir):
        return
    print("README 업데이트 완료.")

    print("\n[3/4] Git 변경사항 스테이징...")
    if not run_command(["git", "add", "."], target_dir):
        return
    print("Git 스테이징 완료.")

    print("\n[4/4] Git 커밋 및 푸시...")
    # 커밋할 내용이 없을 때를 대비하여 예외 처리
    commit_result = run_command(["git", "commit", "-m", COMMIT_MESSAGE], target_dir)
    if not commit_result:
        # 'nothing to commit' 메시지는 정상으로 간주
        # 실제로는 stderr를 파싱하는 것이 더 정확하지만, 여기서는 단순하게 처리
        print("커밋할 내용이 없거나 이미 커밋되었습니다.")

    # 현재 브랜치 이름을 가져와서 push
    current_branch = get_current_branch(target_dir)
    if not current_branch:
        print("오류: 현재 Git 브랜치 이름을 가져올 수 없습니다.")
        return
        
    print(f"현재 브랜치: {current_branch}")
    if not run_command(["git", "push", "--set-upstream", "origin", current_branch], target_dir):
        return
    
    print("\n✨ 모든 동기화 작업이 성공적으로 완료되었습니다!")


if __name__ == "__main__":
    main()
