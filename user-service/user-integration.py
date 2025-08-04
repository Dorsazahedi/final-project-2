import pytest
from app import app
import os
import sqlite3

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_user_registration_and_listing(client):
    # Register a user
    response = client.post("/register", json={"username": "integration_test", "password": "123"})
    assert response.status_code == 201
    assert b"registered" in response.data.lower()

    # Retrieve all users
    response = client.get("/users")
    assert response.status_code == 200
    assert any("integration_test" in str(u) for u in response.json)
