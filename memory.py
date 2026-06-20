import sqlite3
from datetime import datetime

conn = sqlite3.connect(
    "chat_history.db",
    check_same_thread=False
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS chats(
id INTEGER PRIMARY KEY AUTOINCREMENT,
role TEXT,
message TEXT,
timestamp TEXT
)
""")

conn.commit()

def save_chat(role,message):

    cur.execute(
        "INSERT INTO chats(role,message,timestamp) VALUES(?,?,?)",
        (
            role,
            message,
            str(datetime.now())
        )
    )

    conn.commit()

def load_history():

    cur.execute(
        "SELECT role,message FROM chats"
    )

    rows = cur.fetchall()

    return [
        {
            "role":r,
            "content":m
        }
        for r,m in rows
    ]

def clear_chat():

    cur.execute(
        "DELETE FROM chats"
    )

    conn.commit()