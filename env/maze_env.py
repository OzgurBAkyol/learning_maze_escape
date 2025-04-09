# env/maze_env.py

class MazeEnv:
    def __init__(self):
        self.grid_size = 6
        self.start = (0, 0)
        self.goal = (5, 5)
        self.walls = {(1, 1), (2, 2), (3, 3), (4, 2)}
        self.state = self.start

    def reset(self):
        self.state = self.start
        return self.state

    def get_actions(self):
        return ['up', 'down', 'left', 'right']

    def step(self, action):
        x, y = self.state
        if action == 'up': x = max(0, x - 1)
        if action == 'down': x = min(self.grid_size - 1, x + 1)
        if action == 'left': y = max(0, y - 1)
        if action == 'right': y = min(self.grid_size - 1, y + 1)

        if (x, y) in self.walls:
            x, y = self.state  # duvar varsa kal

        self.state = (x, y)

        reward = 1 if self.state == self.goal else -0.1
        done = self.state == self.goal

        return self.state, reward, done
