import pygame
import random
from Resources import helpers
from Resources import config


class MazeBlock:
    def __init__(self, i, j, grid, color=(180, 0, 0), w=50):
        self.x = i                                   # Coordinates
        self.y = j                                   # Coordinates
        self.visited = False
        #            top(0)  r(1)  b(2) l(3)
        self.walls = [True, True, True, True]        # Walls to a cell, They all have 4 walls by default
        self.color = color                           # color of the cell
        self.grid = grid                             # grid the cell is in
        self.W = w                                   # Width of the cell
        self.reward = 0                              # Reward of the cell
        self.thicc = config.WallW                    # Width of the wall

        if color == (255, 255, 0):
            self.reward = 1

    def getNeighbor(self, grid):

        """ Returns a random neighbor"""

        n = []
        rows = grid.shape[0]
        cols = grid.shape[0]

        top = helpers.index(grid, self.x, self.y - 1, rows, cols)
        right = helpers.index(grid, self.x + 1, self.y, rows, cols)
        bottom = helpers.index(grid, self.x, self.y + 1, rows, cols)
        left = helpers.index(grid, self.x - 1, self.y, rows, cols)

        if top != -1:
            if not top.visited:
                n.append(top)

        if right != -1:
            if not right.visited:
                n.append(right)

        if bottom != -1:
            if not bottom.visited:
                n.append(bottom)

        if left != -1:
            if not left.visited:
                n.append(left)

        if len(n) > 0:
            foo = random.randint(0, len(n) - 1)
            return n[foo]
        else:
            return -1

    def render(self, screen):

        """ Renders the walls and the tile on the screen"""

        x = self.x * self.W
        y = self.y * self.W

        if self.visited:
            pygame.draw.rect(
                screen,
                self.color,
                [x, y, self.W, self.W]
            )

        if self.walls[0]:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (x, y), (x + self.W, y),
                self.thicc
            )

        if self.walls[1]:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (x + self.W, y), (x + self.W, y + self.W),
                self.thicc
            )

        if self.walls[2]:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (x + self.W, y + self.W), (x, y + self.W),
                self.thicc
            )

        if self.walls[3]:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (x, y + self.W), (x, y),
                self.thicc
            )
