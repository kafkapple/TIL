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
        if "nothing to commit" in e.stdout or "nothing to commit" in e.stderr:
            print("     커밋할 내용이 없습니다.")
            return True
        if "Already up to date" in e.stdout or "Already up-to-date" in e.stdout:
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

def git_pull_rebase(repo_path):
    """원격 저장소의 변경사항을 pull --rebase로 가져옵니다.
    pull 전에 로컬 저장소를 원격과 동일하게 초기화합니다.
    주의: 이 작업은 로컬의 커밋되지 않은 변경사항과 추적되지 않은 파일을 영구적으로 삭제합니다.
    """
    print("   로컬 저장소 상태를 초기화합니다 (git reset --hard HEAD && git clean -fd).")
    if not run_command(["git", "reset", "--hard", "HEAD"], repo_path):
        return False
    if not run_command(["git", "clean", "-fd"], repo_path):
        return False

    current_branch = get_current_branch(repo_path)
    if not current_branch:
        print("  - 오류: 현재 Git 브랜치 이름을 가져올 수 없습니다.")
        return False
    
    return run_command(["git", "pull", "--rebase", "origin", current_branch], repo_path)

def git_commit_and_push(repo_path):
    """변경된 내용을 add, commit, push 합니다."""
    print("-> 변경사항을 원격 저장소에 푸시합니다...")
    
    # 1. Add
    print(" 1. 변경된 파일들을 스테이징합니다 (add).")
    if not run_command(["git", "add", "."], repo_path):
        return False

    # 2. Commit
    print(" 2. 변경사항을 커밋합니다 (commit).")
    commit_message = f"docs: TIL Sync {datetime.datetime.now().strftime('%Y-%m-%d')}"
    if not run_command(["git", "commit", "-m", commit_message], repo_path):
        return False # 커밋할 내용이 없는 경우도 여기서 True가 반환되어 계속 진행됨

    # 3. Push
    print(" 3. 원격 저장소로 푸시합니다 (push).")
    current_branch = get_current_branch(repo_path)
    if not current_branch:
        print("  - 오류: 현재 Git 브랜치 이름을 가져올 수 없습니다.")
        return False
    if not run_command(["git", "push", "origin", current_branch], repo_path):
        return False
        
    print("   Git 동기화가 성공적으로 완료되었습니다.")
    return True
