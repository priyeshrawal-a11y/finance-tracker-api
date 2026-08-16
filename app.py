from flask import Flask, jsonify, request
from database import (
    get_all_transactions,
    create_transaction,
    delete_transaction,
    update_transaction
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

    required_fields = [
        "name",
        "amount",
        "category",
        "date",
        "transaction_type"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    if not isinstance(data["amount"], (int, float)):
        return jsonify({"error": "Amount must be a number"}), 400

    if data["amount"] <= 0:
        return jsonify({"error": "Amount must be greater than 0"}), 400

    if data["transaction_type"] not in ["Income", "Expense"]:
        return jsonify({
            "error": "Transaction type must be Income or Expense"
        }), 400

    if not data["name"].strip():
        return jsonify({"error": "Name cannot be empty"}), 400

    create_transaction(data)

    return jsonify({
        "message": "Transaction created successfully",
        "transaction": data
    }), 201

@app.route("/transactions/<int:id>", methods=["DELETE"])
def remove_transaction(id):

    deleted = delete_transaction(id)

    if not deleted:
        return jsonify({
            "error": "Transaction not found"
        }), 404

    return jsonify({
        "message": f"Transaction {id} deleted successfully"
    }), 200

@app.route("/transactions/<int:id>", methods=["PUT"])
def update_transaction_route(id):

    data = request.json

    required_fields = [
        "name",
        "amount",
        "category",
        "date",
        "transaction_type"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    updated = update_transaction(id, data)

    if not updated:
        return jsonify({
            "error": "Transaction not found"
        }), 404

    return jsonify({
        "message": "Transaction updated successfully",
        "transaction": data
    }), 200


if __name__ == "__main__":
    app.run(debug=True)


