import numpy as np
import pygame
from Resources import config

grid = np.load(config.OUTPUT_FILE, allow_pickle= True)
rows = grid.shape[0]
cols = grid.shape[0]

pygame.init()
screen = pygame.display.set_mode([1000,1000])
pygame.display.set_caption("Test")


while True:
    for row in range(rows):
        for col in range(cols):
            grid[row, col].render(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(grid[grid.shape[0] - 1, grid.shape[1] - 1].reward)
            pygame.quit()



