import pytest
from src.drone.drone_controller import DroneController

def test_drone_init():
    """
    Test if the DroneController initializes without errors.
    """
    drone = DroneController()
    assert drone is not None

def test_drone_takeoff(mocker):
    """
    Mock the takeoff function to ensure it's called.
    """
    drone = DroneController()
    mocker.patch.object(drone, "take_off")
    drone.take_off()
    drone.take_off.assert_called_once()

def test_drone_land(mocker):
    """
    Mock the land function to ensure it's called.
    """
    drone = DroneController()
    mocker.patch.object(drone, "land")
    drone.land()
    drone.land.assert_called_once()