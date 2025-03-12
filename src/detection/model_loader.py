from ultralytics import YOLO

def load_model():
    """
    Loads the YOLOv8 pre-trained model for object detection.
    """
    return YOLO("yolov8n.pt")

# Global model instance
model = load_model()