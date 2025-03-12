import cv2
import requests
import os

# Load camera URL from environment variables
CAMERA_URL = os.getenv("CAMERA_URL", "rtsp://user:password@192.168.1.100:554/live/ch0")

class IPCamera:
    """
    Handles the video stream from the Wansview 2K Solar Camera.
    Captures frames and sends them to the detection server.
    """
    def __init__(self, url=CAMERA_URL):
        self.url = url
        self.capture = cv2.VideoCapture(self.url)

    def start_stream(self):
        """
        Starts the video stream and sends frames to the detection API.
        """
        while True:
            ret, frame = self.capture.read()
            if not ret:
                print("⚠️ Failed to capture video. Check camera URL.")
                break

            cv2.imshow("Camera Feed", frame)

            # Convert frame to bytes and send to API
            _, img_encoded = cv2.imencode('.jpg', frame)
            requests.post("http://localhost:5000/detect", files={"image": img_encoded.tobytes()})

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    cam = IPCamera()
    cam.start_stream()