import pytest
from app import app, db, Order

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_place_order_success(client):
    res = client.post("/order", json={"user": "sara", "item": "room A"})
    assert res.status_code == 201
    assert b"Order placed" in res.data

def test_place_order_missing_data(client):
    res = client.post("/order", json={"user": "sara"})
    assert res.status_code == 400
