import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_booking_flow(client):
    # Send a valid booking
    data = {"user": "parisa", "destination": "Toronto"}
    response = client.post("/bookings", json=data)
    assert response.status_code == 201
    assert b"confirmed" in response.data.lower()
    assert "booking_id" in response.get_json()
