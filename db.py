import sqlite3

DB_NAME = "prompts.db"

def connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = connect()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            version INTEGER,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()