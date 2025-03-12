from stable_baselines3 import DQN
from src.reinforcement_learning.drone_env import DroneEnv

env = DroneEnv()

# Train using Deep Q-Learning
model = DQN("MlpPolicy", env, verbose=1, learning_rate=0.001, buffer_size=5000, batch_size=32)
model.learn(total_timesteps=50000)

# Save the trained model
model.save("src/reinforcement_learning/trained_dron_model")