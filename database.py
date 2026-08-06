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

    connection.commit()
    connection.close()