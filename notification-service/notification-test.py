<<<<<<< HEAD
import pytest
from app import app

@pytest.fixture
def testing_user():
    app.config["TESTING"] = True
    with app.test_client() as testing_user:
        yield testing_user

def test_notify_ok(testing_user):
    response = testing_user.post("/notify/email", json={"user": "ali", "message": "done. Congratulations!"})
    assert response.status_code == 200
    assert b"email sent" in response.data.lower()

def test_notify_fail(testing_user):
    response = testing_user.post("/notify/email", json={})
    assert response.status_code == 200  # Still 200, service just returns whatever it receives
    assert b"user" in response.data.lower()  # Optionally verify part of response
=======
import pytest
from app import app

@pytest.fixture
def testing_user():
    app.config["TESTING"] = True
    with app.test_client() as testing_user:
        yield testing_user

def test_notify_ok(testing_user):
    response = testing_user.post("/notify/email", json={"user": "ali", "message": "done. Congratulations!"})
    assert response.status_code == 200
    assert b"email sent" in response.data.lower()

def test_notify_fail(testing_user):
    response = testing_user.post("/notify/email", json={})
    assert response.status_code == 200 
    assert b"user" in response.data.lower() 
>>>>>>> f44566b (Final project updates: added order-service, fixed DB, updated README, security)
