import threading
import time
from src.api.server import app
from src.camera.ip_camera import IPCamera
from src.reinforcement_learning.run_agent import main as run_agent

def start_flask_server():
    """
    Starts the Flask API server for handling camera images and detection.
    """
    print("🚀 Starting Flask API Server...")
    app.run(debug=True, host="0.0.0.0", port=5000)

def start_camera_stream():
    """
    Starts the camera stream to capture video and send frames to the detection API.
    """
    print("📸 Starting Camera Stream...")
    camera = IPCamera()
    camera.start_stream()

def start_ai_drone():
    """
    Starts the AI-powered drone patrol using reinforcement learning.
    """
    print("🚁 Starting AI-powered Drone Patrol...")
    run_agent()

if __name__ == "__main__":
    # Start Flask API server in a separate thread
    flask_thread = threading.Thread(target=start_flask_server)
    flask_thread.start()

    # Allow time for the API to initialize before starting other processes
    time.sleep(2)

    # Start the camera and AI drone in separate threads
    camera_thread = threading.Thread(target=start_camera_stream)
    drone_thread = threading.Thread(target=start_ai_drone)

    camera_thread.start()
    drone_thread.start()

    # Wait for all threads to finish
    camera_thread.join()
    drone_thread.join()
    flask_thread.join()