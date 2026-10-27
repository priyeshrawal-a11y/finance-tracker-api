# Finance Tracker API

A personal finance tracking REST API built with Python, Flask and SQLite. This project demonstrates CRUD operations, input validation, database integration and automated testing.

## Features

- Retrieve all financial transactions
- Create transactions with input validation
- Update existing transactions
- Delete transactions
- Store transaction data in an SQLite database
- Automated API tests using pytest

## Technologies

- Python
- Flask
- SQLite
- pytest

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/priyeshrawal-a11y/finance-tracker-api.git
   cd finance-tracker-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install Flask pytest
   ```

4. Initialise the database if required by your application:

   ```bash
   python
   ```

   ```python
   from database import init_db
   init_db()
   exit()
   ```

## Run the API

```bash
python app.py
```

The API will run locally using Flask.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check that the API is running |
| GET | `/transactions` | Retrieve all transactions |
| POST | `/transactions` | Create a transaction |
| PUT | `/transactions/<id>` | Update a transaction |
| DELETE | `/transactions/<id>` | Delete a transaction |

Transactions include a name, amount, category, date and transaction type (`Income` or `Expense`).

## Run the tests

```bash
pytest
```

The automated tests cover API responses, transaction creation, validation, updates and deletion.

## Future improvements

- Add filtering by category and date
- Add transaction summaries and spending reports
- Improve validation and error handling
- Add API documentation and deployment
