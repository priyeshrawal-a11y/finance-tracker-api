import os
import pytest

from app import app
from database import get_connection, init_db

@pytest.fixture
def client():
    if os.path.exists("test_finance.db"):
        os.remove("test_finance.db")

    app.config["DATABASE"] = "test_finance.db"
    init_db(app.config["DATABASE"])

    return app.test_client()

app.config["DATABASE"] = "test_finance.db"

init_db(app.config["DATABASE"])

def test_home(client):

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Finance Tracker API is running!"


def test_get_transactions(client):

    response = client.get("/transactions")

    assert response.status_code == 200
    assert response.is_json


def test_create_transaction(client):

    transaction = {
        "name": "Test Coffee",
        "amount": 4.50,
        "category": "Food",
        "date": "2026-08-16",
        "transaction_type": "Expense"
    }

    response = client.post(
        "/transactions",
        json=transaction
    )

    assert response.status_code == 201
    assert response.is_json


def test_delete_transaction(client):

    transaction = {
        "name": "Delete Test",
        "amount": 10.00,
        "category": "Test",
        "date": "2026-08-16",
        "transaction_type": "Expense"
    }

    create_response = client.post(
        "/transactions",
        json=transaction
    )

    assert create_response.status_code == 201

    transaction_id = create_response.get_json()["transaction"]["id"]

    delete_response = client.delete(
        f"/transactions/{transaction_id}"
    )

    assert delete_response.status_code == 200