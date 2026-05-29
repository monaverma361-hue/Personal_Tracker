import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "data", "document.db")


def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grocery REAL,
            dairy REAL,
            laundry REAL,
            payment_mode TEXT,
            shopping REAL,
            fruit_vegetable REAL,
            other_bills REAL,
            date TEXT
        )
        """
    )

    connection.commit()
    connection.close()
