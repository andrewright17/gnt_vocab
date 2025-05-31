import sqlite3
from sqlite3 import Connection, Error
from vocab.config import DB_PATH

def get_connection() -> Connection | None:
    try:
        conn = sqlite3.connect(DB_PATH)
        #print(DB_PATH)
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
        return None


