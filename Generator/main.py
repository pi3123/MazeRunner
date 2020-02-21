import pygame
import numpy as np
from Resources import helpers
from Resources.Tiles import MazeBlock
from Resources import config

stack = []
grid = np.zeros((config.rows, config.cols), dtype=object)

pygame.init()
screen = pygame.display.set_mode(config.WINDOW_SIZE)
pygame.display.set_caption("Maze")
screen.fill((30, 30, 30))
pygame.display.update()
clock = pygame.time.Clock()

for x in range(config.rows):
    for y in range(config.cols):
        cell = MazeBlock.MazeBlock(x, y, grid, w=config.W)
        grid[x, y] = cell
current = grid[0, 0]


def draw(arr):
    for row in range(config.rows):
        for col in range(config.cols):
            arr[row, col].render(screen)
    pygame.display.update()


def Evolve():
    global current
    current.visited = True
    Next = current.getNeighbor(grid)
    if Next != -1:
        Next.visited = True
        stack.append(current)

        helpers.breakWall(current, Next)
        current = Next

    elif len(stack) > 0:
        current = stack.pop()


while True:
    Evolve()
    draw(grid)
    clock.tick(60)

    if len(stack) == 0:
        np.save(config.OUTPUT_FILE, grid, allow_pickle=True)
        pygame.quit()
        print("Maze stored to "+config.OUTPUT_FILE)
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            np.save(config.OUTPUT_FILE, grid, allow_pickle=True)
            pygame.quit()
            print("Maze stored to "+config.OUTPUT_FILE)
