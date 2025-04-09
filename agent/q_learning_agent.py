# agent/q_learning_agent.py
import numpy as np
from utils.config import *

class QLearningAgent:
    def __init__(self, actions):
        self.q_table = {}  # (state) → [Q values per action]
        self.actions = actions

    def get_qs(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        return self.q_table[state]

    def choose_action(self, state, epsilon):
        if np.random.random() < epsilon:
            return np.random.choice(self.actions)
        else:
            return self.actions[np.argmax(self.get_qs(state))]

    def update(self, state, action, reward, next_state):
        action_idx = self.actions.index(action)
        max_future_q = np.max(self.get_qs(next_state))
        current_q = self.get_qs(state)[action_idx]

        new_q = current_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * max_future_q - current_q)
        self.q_table[state][action_idx] = new_q
