# utils/visualize.py
import pygame
import time

CELL_SIZE = 60
MARGIN = 2
AGENT_COLOR = (30, 144, 255)
GOAL_COLOR = (50, 205, 50)
WALL_COLOR = (178, 34, 34)
PATH_COLOR = (200, 200, 200)
BG_COLOR = (240, 240, 240)

def draw_maze(screen, env, path):
    screen.fill(BG_COLOR)
    for x in range(env.grid_size):
        for y in range(env.grid_size):
            rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE - MARGIN, CELL_SIZE - MARGIN)
            color = BG_COLOR

            if (x, y) in env.walls:
                color = WALL_COLOR
            elif (x, y) == env.goal:
                color = GOAL_COLOR
            elif (x, y) == env.state:
                color = AGENT_COLOR
            elif (x, y) in path:
                color = PATH_COLOR

            pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
