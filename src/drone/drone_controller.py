from dji_sdk import DJIDrone
import time

class DroneController:
    """
    Handles the autonomous control of the DJI Mini 3 drone.
    """
    def __init__(self):
        self.drone = DJIDrone()
        self.drone.connect()

    def take_off(self):
        """Commands the drone to take off."""
        print("🚁 Taking off...")
        self.drone.takeoff()
        time.sleep(5)

    def patrol_area(self):
        """Moves the drone in a square patrol pattern."""
        print("🚁 Patrolling...")
        self.drone.move_forward(30)
        time.sleep(2)
        self.drone.rotate_clockwise(90)
        time.sleep(2)
        self.drone.move_forward(30)

    def land(self):
        """Commands the drone to land."""
        print("🚁 Landing...")
        self.drone.land()

if __name__ == "__main__":
    drone = DroneController()
    drone.take_off()
    drone.patrol_area()
    drone.land()