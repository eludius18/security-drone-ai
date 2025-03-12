import pytest
from stable_baselines3 import DQN
from src.reinforcement_learning.drone_env import DroneEnv

@pytest.fixture
def env():
    """
    Create a test instance of the drone environment.
    """
    return DroneEnv()

def test_environment_reset(env):
    """
    Test if the environment resets correctly.
    """
    state = env.reset()
    assert isinstance(state, list)

def test_rl_training(mocker, env):
    """
    Mock RL training to ensure the model learns without errors.
    """
    mocker.patch.object(DQN, "learn")
    model = DQN("MlpPolicy", env, verbose=1)
    model.learn(100)
    model.learn.assert_called_once()