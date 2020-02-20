import pygame
import numpy as np

W = 50
WIDTH = 1000
HEIGHT = 1000
WINDOW_SIZE = [WIDTH, HEIGHT]
cols = int(WIDTH / W)
rows = int(HEIGHT / W)
WHITE = (255, 255, 255)

grid = np.zeros((rows, cols), dtype=object)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Maze")
screen.fill((90, 90, 90))
clock = pygame.time.Clock()


class Cell:

    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]

    def show(self):
        x = self.x * W
        y = self.y * W
        if self.walls[0]:
            pygame.draw.line(
                screen,
                WHITE,
                (x, y), (x + W, y))

        if self.walls[1]:
            pygame.draw.line(
                screen,
                WHITE,
                (x + W, y), (x + W, y + W))

        if self.walls[2]:
            pygame.draw.line(
                screen,
                WHITE,
                (x + W, y + W), (x, y + W)
            )

        if self.walls[3]:
            pygame.draw.line(
                screen,
                WHITE,
                (x, y + W), (x, y)
            )


for x in range(rows):
    for y in range(cols):
        cell = Cell(x, y, W)
        grid[x, y] = cell


def draw():
    for row in range(rows):
        for col in range(cols):
            grid[row, col].show()


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
