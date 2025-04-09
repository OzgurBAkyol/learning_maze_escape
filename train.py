# train.py
from env.maze_env import MazeEnv
from agent.q_learning_agent import QLearningAgent
from utils.config import *
import matplotlib.pyplot as plt

env = MazeEnv()
agent = QLearningAgent(env.get_actions())

eps = EPSILON
rewards = []

for episode in range(NUM_EPISODES):
    state = env.reset()
    total_reward = 0

    for _ in range(MAX_STEPS_PER_EPISODE):
        action = agent.choose_action(state, eps)
        next_state, reward, done = env.step(action)
        agent.update(state, action, reward, next_state)
        state = next_state
        total_reward += reward

        if done:
            break

    eps = max(MIN_EPSILON, eps * EPSILON_DECAY)
    rewards.append(total_reward)

# plot reward
plt.plot(rewards)
plt.title("Episodic Rewards")
plt.show()


import pickle
with open("q_table.pkl", "wb") as f:
    pickle.dump(agent.q_table, f)