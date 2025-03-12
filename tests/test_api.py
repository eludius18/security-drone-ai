import pytest
from src.api.server import app

@pytest.fixture
def client():
    """
    Provides a test client for the Flask API.
    """
    app.config["TESTING"] = True
    return app.test_client()

def test_api_home(client):
    """
    Test if the API server is running.
    """
    response = client.get("/")
    assert response.status_code == 200

def test_detection_endpoint(client, mocker):
    """
    Mock the detection process to test the API response.
    """
    mocker.patch("src.detection.detector.detect_objects", return_value=(True, (0,0,50,50)))
    response = client.post("/detect", data={"image": b"fake_image_data"})
    assert response.status_code == 200
    assert response.json["status"] == "ok"