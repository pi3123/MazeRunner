import numpy as np
import pygame
from Resources import helpers

'''
top = helpers.index(grid, self.x, self.y - 1, rows, cols)
right = helpers.index(grid, self.x + 1, self.y, rows, cols)
bottom = helpers.index(grid, self.x, self.y + 1, rows, cols)
left = helpers.index(grid, self.x - 1, self.y, rows, cols)
'''


class Player:
    def __init__(self, grid, color=(0, 180, 0)):
        self.grid = grid
        self.color = color
        self.W = grid[0, 0].W

        self.x = np.random.randint(0, grid.shape[0])
        self.y = 0
        self.done = False
        self.reward = grid[self.x, self.y].reward

    def step(self, choice):
        if choice == 0:
            if self.possible(self.grid, choice):
                self.y -= 1
        elif choice == 1:
            if self.possible(self.grid, choice):
                self.x += 1
        elif choice == 2:
            if self.possible(self.grid, choice):
                self.y += 1
        elif choice == 3:
            if self.possible(self.grid, choice):
                self.x -= 1

        self.reward = helpers.getReward(self.grid, self.x, self.y)
        if self.reward != 0:
            self.done = True
        return (self.x, self.y), self.reward, self.done

    def render(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            [self.x * self.W, self.y * self.W, self.W, self.W],
        )

    def possible(self, grid, choice):
        if not grid[self.x, self.y].walls[choice]:
            return True
        else:
            return False
