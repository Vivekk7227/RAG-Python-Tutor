import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(REPO_ROOT / "backend"))

from app.config.supabase_client import supabase

def run_sql_file(filepath: str):
    with open(filepath, 'r') as f:
        query = f.read()
    try:
        res = supabase.rpc("exec_sql", {"sql_query": query}).execute()
        print("Success:", res.data)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    run_sql_file(str(Path(__file__).resolve().parent / "update_rls.sql"))
