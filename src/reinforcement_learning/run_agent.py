import gym
from stable_baselines3 import DQN
from src.reinforcement_learning.drone_env import DroneEnv

def main():
    """
    Loads the trained reinforcement learning model and runs the drone in an optimized patrol mode.
    """
    env = DroneEnv()
    model = DQN.load("src/reinforcement_learning/trained_dron_model")

    obs = env.reset()
    done = False

    print("🚀 Running the AI-powered drone agent...")

    while not done:
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)

    print("🏁 AI patrol completed.")

if __name__ == "__main__":
    main()