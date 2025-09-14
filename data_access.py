import sqlite3
from datetime import datetime

DB_NAME = "parking.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        model TEXT,
        color TEXT,
        plate TEXT UNIQUE,
        entry_time TEXT,
        exit_time TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_car(name, model, color, plate):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor.execute(
            "INSERT INTO cars (name, model, color, plate, entry_time) VALUES (?, ?, ?, ?, ?)",
            (name, model, color, plate, entry_time)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def remove_car(plate):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    exit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("UPDATE cars SET exit_time=? WHERE plate=?", (exit_time, plate))
    cursor.execute("DELETE FROM cars WHERE plate=?", (plate,))
    conn.commit()
    conn.close()

def get_all_cars():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, model, color, plate, entry_time, exit_time FROM cars")
    cars = cursor.fetchall()
    conn.close()
    return cars
