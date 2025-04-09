# play.py
import pygame
from env.maze_env import MazeEnv
from agent.q_learning_agent import QLearningAgent
from utils.config import *
from utils.visualize import draw_maze

def play_with_pygame(agent):
    pygame.init()
    env = MazeEnv()
    screen = pygame.display.set_mode((env.grid_size * 60, env.grid_size * 60))
    pygame.display.set_caption("Q-Learning Maze")

    state = env.reset()
    path = [state]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        action = agent.choose_action(state, epsilon=0.0)
        next_state, reward, done = env.step(action)
        path.append(next_state)

        draw_maze(screen, env, path)
        time.sleep(0.3)  # biraz yavaş görünsün

        state = next_state
        if done:
            print("🎉 Agent reached the goal!")
            time.sleep(1.5)
            running = False

    pygame.quit()

# main blok
if __name__ == "__main__":
    agent = QLearningAgent(['up', 'down', 'left', 'right'])

    # Q-table örnek dolu değilse önce train.py ile eğit
    # train.py sonrası pickle ile Q-table yükleyebilirsin
    # burada test için eğitimden sonra çağrılmalı

    play_with_pygame(agent)
