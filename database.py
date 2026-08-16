import sqlite3


def get_connection():
    return sqlite3.connect("finance.db")


def get_all_transactions():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    connection.close()

    return transactions


def create_transaction(data):
    connection = get_connection()
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
    connection.close()


def delete_transaction(id):
    connection = get_connection()
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

def update_transaction(id, data):
    connection = get_connection()
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