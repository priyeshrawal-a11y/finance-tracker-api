class Transaction:
    def __init__(self, name, amount, category, date, transaction_type):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
        self.transaction_type = transaction_type