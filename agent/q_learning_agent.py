# agent/q_learning_agent.py
import numpy as np
from utils.config import *

class QLearningAgent:
    def __init__(self, actions):
        self.q_table = {} # ajanın öğrenmesi için Q table
        self.actions = actions # yapılabilcek hareketler

    def get_qs(self, state): # yoksa aksiyon sayısı kadar liste oluşturur
        if state not in self.q_table:
            self.q_table[state] = np.zeros(len(self.actions))
        return self.q_table[state]

    def choose_action(self, state, epsilon):
        if np.random.random() < epsilon: # epsilon oranında ajan rastgele bir hareket seçer
            return np.random.choice(self.actions)
        else:
            return self.actions[np.argmax(self.get_qs(state))] # yani bazen rastgele bazen öğrendiği en iyi hareketi yapıyo


    def update(self, state, action, reward, next_state): # seçilen aksiyonun indexini bulur
        action_idx = self.actions.index(action) # bir sonraki state'deki en yüksek Q değeri
        max_future_q = np.max(self.get_qs(next_state)) # şuanki state'deki seçilen aksiyonun Q değeri
        current_q = self.get_qs(state)[action_idx]

        new_q = current_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * max_future_q - current_q)
        self.q_table[state][action_idx] = new_q
        # learning rate ne kadar hızlı öğrenceğini belirler
        # discount factor ise gelecekteki ödüllerin ne kadar önemli olduğunu belirler
