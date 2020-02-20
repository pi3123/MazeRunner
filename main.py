import pygame
import numpy as np
from Tiles import helpers
from Tiles import Cell

W = 50
WIDTH = 1000
HEIGHT = 1000
WINDOW_SIZE = [WIDTH, HEIGHT]
rows = int(HEIGHT / W)
cols = int(WIDTH / W)
WHITE = (255, 255, 255)
stack = []
grid = np.zeros((rows, cols), dtype=object)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Maze")
screen.fill((30, 30, 30))
pygame.display.update()
clock = pygame.time.Clock()

for x in range(rows):
    for y in range(cols):
        cell = Cell.Cell(x, y, grid, w=W)
        grid[x, y] = cell
current = grid[0, 0]


def draw(arr):
    for row in range(rows):
        for col in range(cols):
            arr[row, col].show(screen)
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


done = False
while not done:
    Evolve()
    draw(grid)
    clock.tick(60)

    if len(stack) == 0:
        np.save("maze", grid, allow_pickle=True)
        pygame.quit()
        print("maze made and stored")
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            np.save("maze", grid, allow_pickle=True)
            pygame.quit()
            print("maze made and stored")


