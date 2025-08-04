<<<<<<< HEAD
import pytest
import requests_mock
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_booking_triggers_notification(client):
    with requests_mock.Mocker() as m:
        m.post("http://notification-service:5002/notify/email", status_code=200)
        response = client.post("/bookings", json={"user": "ali", "destination": "Paris"})
        assert response.status_code == 201
        assert m.called
=======
import pytest
import requests_mock
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_booking_triggers_notification(client):
    with requests_mock.Mocker() as m:
        m.post("http://notification-service:5002/notify/email", status_code=200)                  #THIS

        response = client.post("/bookings", json={"user": "ali", "destination": "Paris"})
        assert response.status_code == 201
        assert m.called
>>>>>>> f44566b (Final project updates: added order-service, fixed DB, updated README, security)
