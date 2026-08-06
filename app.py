from flask import Flask, jsonify, request
from database import (
    get_all_transactions,
    create_transaction,
    delete_transaction
)

app = Flask(__name__)


@app.route("/")
def home():
    return "Finance Tracker API is running!"


@app.route("/transactions")
def get_transactions():

    transactions = get_all_transactions()

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
def add_transaction():

    data = request.json

    create_transaction(data)

    return jsonify({
        "message": "Transaction created successfully",
        "transaction": data
    })


@app.route("/transactions/<int:id>", methods=["DELETE"])
def remove_transaction(id):

    delete_transaction(id)

    return jsonify({
        "message": f"Transaction {id} deleted successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)