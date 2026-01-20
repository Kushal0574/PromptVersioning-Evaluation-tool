from db import connect, init_db

def add_prompt(name, content):
    init_db()
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT MAX(version) FROM prompts WHERE name=?", (name,))
    row = c.fetchone()
    version = (row[0] or 0) + 1

    c.execute(
        "INSERT INTO prompts (name, version, content) VALUES (?, ?, ?)",
        (name, version, content)
    )
    conn.commit()
    conn.close()
    print(f"Added prompt '{name}' v{version}")

def list_prompts():
    init_db()
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT name, version FROM prompts")
    rows = c.fetchall()
    conn.close()
    return rows