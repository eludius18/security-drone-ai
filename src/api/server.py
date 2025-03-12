from flask import Flask, request
from src.detection.detector import detect_objects
from src.drone.drone_controller import DroneController
from src.alerts.telegram_alert import send_alert

app = Flask(__name__)
drone = DroneController()

@app.route("/detect", methods=["POST"])
def detect():
    """
    API Endpoint to receive images and detect intruders.
    """
    image = request.files["image"].read()
    is_intruder, _ = detect_objects(image)

    if is_intruder:
        send_alert("intruder.jpg")
        print("🚨 Intruder detected! Deploying drone...")
        drone.take_off()
        drone.patrol_area()
        drone.land()

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)