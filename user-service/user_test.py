import pytest
from app import app, init_db  

@pytest.fixture
def client():
    init_db()  # 🛠 Initialize DB before tests
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_register_success(client):
    response = client.post("/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert b"User registered" in response.data

def test_register_missing_fields(client):
    response = client.post("/register", json={})
    assert response.status_code == 400
    assert b"Username and password are required" in response.data
