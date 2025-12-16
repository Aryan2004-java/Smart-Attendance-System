import sqlite3

DB_PATH = "database/attendance.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

# ---------------- USERS ----------------

def add_user(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return user_id

def get_user_by_id(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE id = ? AND active = 1", (user_id,))
    user = cur.fetchone()
    conn.close()
    return user

def get_user_by_name(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE name = ? AND active = 1", (name,))
    user = cur.fetchone()
    conn.close()
    return user

def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE active = 1")
    users = cur.fetchall()
    conn.close()
    return users

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET active = 0 WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

# ---------------- ATTENDANCE ----------------

def log_attendance(user_id, timestamp):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO attendance (user_id, timestamp) VALUES (?, ?)",
        (user_id, timestamp)
    )
    conn.commit()
    conn.close()

def get_attendance():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT users.name, attendance.timestamp
        FROM attendance
        JOIN users ON attendance.user_id = users.id
        ORDER BY attendance.timestamp DESC
    """)
    records = cur.fetchall()
    conn.close()
    return records

def reset_attendance():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM attendance")
    conn.commit()
    conn.close()
