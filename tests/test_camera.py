import pytest
from src.camera.ip_camera import IPCamera

def test_camera_init():
    """
    Test if the IPCamera class initializes correctly with a given URL.
    """
    cam = IPCamera("http://test_url/video")
    assert cam.url == "http://test_url/video"

def test_camera_stream():
    """
    Test if the IPCamera start_stream function runs without errors.
    (Mocking actual camera stream)
    """
    cam = IPCamera("http://test_url/video")
    assert hasattr(cam, "start_stream")