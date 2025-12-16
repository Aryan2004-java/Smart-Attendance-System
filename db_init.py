import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/attendance.db")
cur = conn.cursor()

# Users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    active INTEGER DEFAULT 1
)
""")

# Attendance table
cur.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    timestamp TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

conn.commit()
conn.close()

print("Database initialized successfully.")
