import sqlite3
import os

def get_connection():
    db_path = os.getenv("SQLITE_DB_PATH", "bookvault.db")
    conn = sqlite3.connect(db_path, check_same_thread=False)
    return conn
