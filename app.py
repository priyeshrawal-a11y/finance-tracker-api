from flask import Flask, jsonify, request
import sqlite3 

app = Flask(__name__)


@app.route("/")
def home():
    return "Finance Tracker API is running!"

@app.route("/transactions")
def get_transactions():
    connection = sqlite3.connect('finance.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    
    transactions_list = []

    for transaction in transactions:
        transaction_dict = {
            "id": transaction[0],
            "name": transaction[1],
            "amount": transaction[2],
            "category": transaction[3],
            "date": transaction[4],
            "transaction_type": transaction[5]
        }

        transactions_list.append(transaction_dict)

    return jsonify(transactions_list)

@app.route("/transactions", methods=["POST"])
def create_transaction():
    data = request.json

    connection = sqlite3.connect('finance.db')
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO transactions (name, amount, category, date, transaction_type)
    VALUES (?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["amount"],
        data["category"],
        data["date"],
        data["transaction_type"]
    ))

    connection.commit()

    return jsonify(data)

@app.route("/transactions/<int:id>", methods=["DELETE"])
def delete_transaction(id):
    connection = sqlite3.connect("finance.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM transactions WHERE id=?", (id,))
    connection.commit()
    connection.close()

    return jsonify({
    "message": f"Transaction {id} deleted successfully."
})

if __name__ == "__main__":
    app.run(debug=True)

