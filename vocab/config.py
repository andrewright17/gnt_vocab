import os
import sqlite3

def get_db_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, '..'))
    return os.path.join(repo_root, 'data', 'gnt.db')

DB_PATH = get_db_path()
