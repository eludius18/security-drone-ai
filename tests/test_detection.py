import pytest
from src.detection.detector import detect_objects

def test_detection():
    """
    Test if the detection function correctly returns a boolean and bounding box.
    """
    sample_image = "test_image.jpg"  # Placeholder for a test image
    result, bbox = detect_objects(sample_image)
    assert isinstance(result, bool)
    assert isinstance(bbox, (tuple, type(None)))