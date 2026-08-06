import sqlite3

def get_connection():
    return sqlite3.connect("finance.db")


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL,
        transaction_type TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()