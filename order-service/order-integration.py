import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_create_and_get_orders(client):
    # Create an order
    response = client.post("/orders", json={
        "user": "ali",
        "product": "laptop"
    })
    assert response.status_code == 201
    assert b"confirmed" in response.data.lower()

    # Get all orders
    response = client.get("/orders")
    assert response.status_code == 200
    assert any("laptop" in str(order) for order in response.json)

