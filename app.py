from flask import Flask, jsonify
import sqlite3 

app = Flask(__name__)
connection = sqlite3.connect('finance.db')
cursor = connection.cursor()

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

class Transaction:
    def __init__(self, name, amount, category, date, transaction_type):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
        self.transaction_type = transaction_type

chocolate = Transaction("Chocolate", 5.0, "Food", "2026-07-01", "Expense")
print(chocolate.name, chocolate.amount)  # Output: Chocolate 5.0

cursor.execute('''
create table if not exists transactions (
    id integer primary key,  
    name TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL,
    transaction_type TEXT NOT NULL
);''')
connection.commit()

#cursor.execute("""
   # INSERT INTO transactions (name, amount, category, date, transaction_type)
   # VALUES (?, ?, ?, ?, ?)
#""", ("Chocolate", 5.00, "Food", "2026-07-01", "Expense"))
#connection.commit()

cursor.execute("SELECT * FROM transactions")
transactions = cursor.fetchall() 
print(transactions)  # Output: [(1, 'Chocolate', 5.0, 'Food', '2026-07-01', 'Expense')]

if __name__ == "__main__":
    app.run(debug=True)

