import numpy as np
from Resources import helpers
import Resources.Tiles.Player as Cell
from Resources import config
import pygame

# PyGame setup
pygame.init()
screen = pygame.display.set_mode([config.WIDTH,config.HEIGHT])
pygame.display.set_caption("MazeSolver")
pygame.display.update()
clock = pygame.time.Clock()


#  Setup the variables
grid = np.load("X:\Projects\MazeRunner\Resources\maze.npy", allow_pickle=True)
current = Cell.Player(grid)
NewState = (current.x, current.y)
reward = current.reward

# set goal
goal = grid[grid.shape[0] - 1, grid.shape[1] - 1]
goal.color = (255, 255, 0)
goal.reward = 1

helpers.drawMaze(grid,screen)


done = False
while not done:
    current.render(screen)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        reward = current.reward

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                NewState, reward, done = current.step(0)

            if event.key == pygame.K_RIGHT:
                NewState, reward, done = current.step(1)

            if event.key == pygame.K_DOWN:
                NewState, reward, done = current.step(2)

            if event.key == pygame.K_LEFT:
                NewState, reward, done = current.step(3)


            helpers.drawMaze(grid,screen)
            print(done)
