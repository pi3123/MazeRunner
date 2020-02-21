import pygame
import random
from Resources import helpers


class MazeBlock:
    def __init__(self, i, j, grid, color=(180, 0, 0), w=50):
        self.x = i
        self.y = j
        #            top(0)  r(1)  b(2) l(3)
        self.walls = [True, True, True, True]
        self.visited = False
        self.color = color
        self.grid = grid
        self.W = w
        self.reward = 0

        if color == (255, 255, 0):
            self.reward = 1

    def getNeighbor(self, grid):
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
        x = self.x * self.W
        y = self.y * self.W
        if self.reward == 1:
            self.color = (255, 255, 0)
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
                5
            )

        if self.walls[1]:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (x + self.W, y), (x + self.W, y + self.W),
                5
            )

        if self.walls[2]:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (x + self.W, y + self.W), (x, y + self.W),
                5
            )

        if self.walls[3]:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (x, y + self.W), (x, y),
                5
            )
