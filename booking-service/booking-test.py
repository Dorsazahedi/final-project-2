import pytest
from app import app

@pytest.fixture
def testing_user():
    app.config["TESTING"] = True
    with app.test_client() as testing_user:
        yield testing_user

def test_booking_fail(testing_user):
    """Should return 400 if user or destination is missing."""
    response = testing_user.post("/bookings", json={})
    assert response.status_code == 400
    assert b"missing" in response.data.lower()

def test_booking_ok(testing_user):
    """Should return 201 and include 'confirmed' in the response if valid."""
    response = testing_user.post("/bookings", json={
        "user": "ali",
        "destination": "London"
    })
    assert response.status_code == 201
    assert b"confirmed" in response.data.lower()
