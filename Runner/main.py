import numpy as np
from Resources import helpers
import Resources.Tiles.Player as Cell
from Resources import config
import pygame

pygame.init()
screen = pygame.display.set_mode(config.WINDOW_SIZE)
pygame.display.set_caption("MazeSolver")
pygame.display.update()
clock = pygame.time.Clock()
grid = np.load("X:\Projects\MazeRunner\Resources\maze.npy", allow_pickle=True)


def drawMaze(arr):
    for row in range(config.rows):
        for col in range(config.cols):
            arr[row, col].render(screen)
    pygame.display.update()


current = Cell.Player(grid)
grid[grid.shape[0] - 1, grid.shape[1] - 1].reward = 1
drawMaze(grid)

done = False
while not done:
    current.render(screen)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if grid[current.x, current.y].color == (255, 255, 0):
            pygame.quit()
            print(grid[current.x, current.y].reward)
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current.step(0)

            if event.key == pygame.K_RIGHT:
                current.step(1)

            if event.key == pygame.K_DOWN:
                current.step(2)

            if event.key == pygame.K_LEFT:
                current.step(3)
        print(grid[current.x,current.y].walls)
