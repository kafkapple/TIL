import subprocess
import datetime

def run_command(command, working_dir):
    """지정된 디렉토리에서 셸 명령을 실행하고 결과를 출력합니다."""
    print(f"  > git {' '.join(command[1:])}")
    try:
        result = subprocess.run(
            command, cwd=working_dir, text=True, capture_output=True, check=True
        )
        if result.stdout.strip():
            print(f"     {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        # 커밋할 내용이 없는 경우는 성공으로 간주
        if "nothing to commit" in e.stdout or "nothing to commit" in e.stderr:
            print("     커밋할 내용이 없습니다.")
            return True
        # 이미 최신 상태인 경우도 성공으로 간주
        if "Already up to date" in e.stdout:
            print("     이미 최신 상태입니다.")
            return True
        print(f"  - 오류 (종료 코드: {e.returncode}):\n{e.stderr or e.stdout}")
        return False
    except FileNotFoundError:
        print(f"  - 오류: '{command[0]}' 명령을 찾을 수 없습니다.")
        return False

def get_current_branch(working_dir):
    """현재 Git 브랜치 이름을 가져옵니다."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=working_dir, check=True, text=True, capture_output=True
        )
        return result.stdout.strip()
    except Exception:
        return None

def git_sync(repo_path):
    """Git 저장소를 원격과 동기화합니다 (pull, add, commit, push)."""
    print("-> Git 동기화 시작...")
    
    current_branch = get_current_branch(repo_path)
    if not current_branch:
        print("  - 오류: 현재 Git 브랜치 이름을 가져올 수 없습니다.")
        return

    # 1. Pull (Rebase)
    print(" 1. 원격 저장소의 변경사항을 가져옵니다 (pull).")
    if not run_command(["git", "pull", "--rebase", "origin", current_branch], repo_path):
        print("  - Pull 실패. 동기화를 중단합니다.")
        return

    # 2. Add
    print(" 2. 변경된 파일들을 스테이징합니다 (add).")
    if not run_command(["git", "add", "."], repo_path):
        return

    # 3. Commit
    print(" 3. 변경사항을 커밋합니다 (commit).")
    commit_message = f"docs: TIL Sync {datetime.datetime.now().strftime('%Y-%m-%d')}"
    if not run_command(["git", "commit", "-m", commit_message], repo_path):
        return

    # 4. Push
    print(" 4. 원격 저장소로 푸시합니다 (push).")
    if not run_command(["git", "push", "origin", current_branch], repo_path):
        return
        
    print("   Git 동기화가 성공적으로 완료되었습니다.")
