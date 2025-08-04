<<<<<<< HEAD
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_register_login_profile_flow(client):
    # Register a user
    register_response = client.post("/register", json={
        "username": "reza",
        "password": "123456"
    })
    assert register_response.status_code == 201
    assert b"registered successfully" in register_response.data

    # Login with that user
    login_response = client.post("/login", json={
        "username": "reza",
        "password": "123456"
    })
    assert login_response.status_code == 200
    assert b"Welcome back" in login_response.data

    # Get the profile
    profile_response = client.get("/profile/reza")
    assert profile_response.status_code == 200
    assert profile_response.json["username"] == "reza"
=======
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_register_login_profile_flow(client):
    register_response = client.post("/register", json={
        "username": "reza",
        "password": "123456"
    })
    assert register_response.status_code == 201
    assert b"registered successfully" in register_response.data

    login_response = client.post("/login", json={
        "username": "reza",
        "password": "123456"
    })
    assert login_response.status_code == 200
    assert b"Welcome back!" in login_response.data

    # Get the profile
    profile_response = client.get("/profile/reza")
    assert profile_response.status_code == 200
    assert profile_response.json["username"] == "reza"
>>>>>>> f44566b (Final project updates: added order-service, fixed DB, updated README, security)
