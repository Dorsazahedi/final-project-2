import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_notify_email_success(client):

    response = client.post("/notify/email", json={
        "user": "ali@example.com",
        "message": "Your booking is confirmed!congratulations!"
    })
    assert response.status_code == 200
    assert response.json["status"] == "email sent"
    assert response.json["user"] == "ali@example.com"

def test_notify_email_missing_fields(client):

    response = client.post("/notify/email", json={})
    assert response.status_code == 200 
    assert "user" in response.json 
