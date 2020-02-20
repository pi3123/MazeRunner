import numpy as np
import pygame

grid = np.load("maze.npy", allow_pickle= True)
rows = grid.shape[0]
cols = grid.shape[0]

pygame.init()
screen = pygame.display.set_mode([1000,1000])
pygame.display.set_caption("Test")


while True:
    for row in range(rows):
        for col in range(cols):
            grid[row, col].show(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
