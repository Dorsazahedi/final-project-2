<<<<<<< HEAD
import pytest
from app import app

@pytest.fixture
def testing_user():
    app.config["TESTING"] = True
    with app.test_client() as testing_user:
        yield testing_user

def test_booking_fail(testing_user):
    response = testing_user.post("/bookings", json={})  # ✅ fixed path
    assert response.status_code == 400


def test_booking_ok(testing_user):
    response = testing_user.post("/bookings", json={"user": "ali", "destination": "London"})  # ✅ correct key
    assert response.status_code == 201
    assert b"confirmed" in response.data.lower()
=======
import pytest
from app import app

@pytest.fixture
def testing_user():
    app.config["TESTING"] = True
    with app.test_client() as testing_user:
        yield testing_user

def test_booking_fail(testing_user):
    response = testing_user.post("/bookings", json={}) 
    assert response.status_code == 400


def test_booking_ok(testing_user):
    response = testing_user.post("/bookings", json={"user": "ali", "destination": "London"})
    assert response.status_code == 201
    assert b"confirmed" in response.data.lower()
>>>>>>> f44566b (Final project updates: added order-service, fixed DB, updated README, security)
