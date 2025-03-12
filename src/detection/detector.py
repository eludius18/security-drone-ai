import cv2
import numpy as np
from src.detection.model_loader import model

def detect_objects(image):
    """
    Detects objects in an image using YOLOv8.

    :param image: Input image
    :return: Tuple (bool: is_intruder_detected, BoundingBox)
    """
    results = model(image)
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            label = model.names[int(box.cls[0])]

            if label == "person":  # Detect human intruders
                return True, (x1, y1, x2, y2)

    return False, None
