import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "healthy"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()
    assert data["application"] == "Fintech Demo"
    assert data["status"] == "running"


def test_successful_transaction():
    client = app.test_client()

    response = client.post(
        "/transaction",
        json={"amount": 1000}
    )

    assert response.status_code == 201

    data = response.get_json()
    assert data["status"] == "success"
    assert data["amount"] == 1000


def test_invalid_transaction():
    client = app.test_client()

    response = client.post(
        "/transaction",
        json={"amount": -100}
    )

    assert response.status_code == 400


def test_get_transactions():
    client = app.test_client()

    response = client.get("/transactions")

    assert response.status_code == 200

    data = response.get_json()
    assert data["count"] == 2
    assert len(data["transactions"]) == 2