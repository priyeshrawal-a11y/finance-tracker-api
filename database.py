import sqlite3


def get_connection(database="finance.db"):
    return sqlite3.connect(database)


def get_all_transactions(database="finance.db"):
    connection = get_connection(database)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    connection.close()

    return transactions


def create_transaction(data, database="finance.db"):
    connection = get_connection(database)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO transactions
    (name, amount, category, date, transaction_type)
    VALUES (?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["amount"],
        data["category"],
        data["date"],
        data["transaction_type"]
    ))

    connection.commit()

    transaction_id = cursor.lastrowid

    connection.close()

    return transaction_id


def delete_transaction(id, database="finance.db"):
    connection = get_connection(database)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM transactions WHERE id=?",
        (id,)
    )

    if cursor.rowcount == 0:
        connection.close()
        return False

    connection.commit()
    connection.close()

    return True

def update_transaction(id, data, database="finance.db"):
    connection = get_connection(database)
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE transactions
    SET name = ?,
        amount = ?,
        category = ?,
        date = ?,
        transaction_type = ?
    WHERE id = ?
    """, (
        data["name"],
        data["amount"],
        data["category"],
        data["date"],
        data["transaction_type"],
        id
    ))

    if cursor.rowcount == 0:
        connection.close()
        return False

    connection.commit()
    connection.close()

    return True


def init_db(database="finance.db"):
    connection = get_connection(database)
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