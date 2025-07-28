import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.get_json() == {"message": "pong"}

def test_two(client):
    response = client.get("/fibs/2")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "1"

def test_ten(client):
    response = client.get("/fibs/10")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "55"

def test_upper_limit(client):
    response = client.get("/fibs/20578")
    assert response.status_code == 422
    assert response.get_json()["message"] == "ValueError: n=20578 is too large. Please use a number smaller than 20578"
