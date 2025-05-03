
import sqlite3

def connect():
    conn = sqlite3.connect("hostel.db")
    cur = conn.cursor()
    return conn, cur

def create_tables():
    conn, cur = connect()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT,
            age INTEGER,
            room TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_no TEXT,
            capacity INTEGER,
            occupied INTEGER DEFAULT 0
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            amount REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_student(id, name, age, room):
    conn, cur = connect()
    cur.execute("INSERT INTO students (id, name, age, room) VALUES (?, ?, ?, ?)", (id, name, age, room))
    conn.commit()
    conn.close()

def view_students():
    conn, cur = connect()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_student(id):
    conn, cur = connect()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

def search_student(keyword):
    conn, cur = connect()
    query = """
        SELECT * FROM students
        WHERE id LIKE ? OR name LIKE ? OR age LIKE ? OR room LIKE ?
    """
    like_keyword = f"%{keyword}%"
    cur.execute(query, (like_keyword, like_keyword, like_keyword, like_keyword))
    rows = cur.fetchall()
    conn.close()
    return rows
