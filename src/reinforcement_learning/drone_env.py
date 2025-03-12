import gym
import numpy as np
from gym import spaces
from src.drone.drone_controller import DroneController

class DroneEnv(gym.Env):
    """
    Custom reinforcement learning environment for drone patrol optimization.
    """
    def __init__(self):
        super(DroneEnv, self).__init__()
        self.drone = DroneController()

        # Actions: 0 - Left, 1 - Right, 2 - Forward, 3 - Land
        self.action_space = spaces.Discrete(4)
        
        # Observations: [x, y, z, distance_to_object, threat_detected]
        self.observation_space = spaces.Box(low=np.array([0, 0, 0, 0, 0]), high=np.array([100, 100, 100, 50, 1]), dtype=np.float32)

    def reset(self):
        """Resets the environment (drone takes off)."""
        self.drone.take_off()
        return np.array([0, 0, 10, 50, 0])

    def step(self, action):
        """
        Defines how the environment responds to actions.
        """
        reward = -1  # Small penalty for every step

        if action == 0:
            self.drone.rotate_counter_clockwise(15)
        elif action == 1:
            self.drone.rotate_clockwise(15)
        elif action == 2:
            self.drone.move_forward(30)
        elif action == 3:
            self.drone.land()
            return self.get_state(), reward, True, {}

        # Simulate obstacle distance and threat probability
        obstacle_distance = np.random.randint(5, 50)
        is_threat = np.random.choice([0, 1], p=[0.9, 0.1])  # 10% probability of a threat

        if is_threat:
            reward += 10  # Reward for detecting a threat

        if obstacle_distance < 10:
            reward -= 10  # Penalty for hitting an obstacle

        return self.get_state(), reward, False, {}

    def get_state(self):
        """
        Returns the current state representation.
        """
        return np.array([np.random.randint(0, 100), np.random.randint(0, 100), 10, np.random.randint(5, 50), np.random.choice([0, 1])])
