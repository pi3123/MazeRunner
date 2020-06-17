import pygame,sys
import numpy as np
from Resources import helpers, config
from Resources.Tiles import MazeBlock
sys.setrecursionlimit(10000)

# PyGame stuff
pygame.init()
screen = pygame.display.set_mode([config.WIDTH, config.HEIGHT])
pygame.display.set_caption("Maze")
screen.fill((30, 30, 30))
pygame.display.update()
clock = pygame.time.Clock()


def Evolve(current, stack, grid):

    """ Makes the maze by getting the random neighbor """

    run = True
    if run:
        current.visited = True
        Next = current.getNeighbor(grid)
        if Next != -1:
            Next.visited = True
            stack.append(current)

            helpers.breakWall(current, Next)
            current = Next

        elif len(stack) > 0:
            current = stack.pop()
    if len(stack) != 0:
        Evolve(current, stack, grid)
    else:
        run = False


def main():

    """ Runs the Evolve method """

    # Setup
    stack = []
    grid = np.zeros((config.rows, config.cols), dtype=object)
    for x in range(config.rows):
        for y in range(config.cols):
            cell = MazeBlock.MazeBlock(x, y, grid, w=config.W)
            grid[x, y] = cell
    current = grid[0, 0]

    # Draw the maze
    Evolve(current, stack, grid)
    helpers.drawMaze(grid, screen)
    clock.tick(60)

    # Save the maze
    np.save(config.OUTPUT_FILE, grid, allow_pickle=True)
    pygame.quit()
    print("Maze stored to " + config.OUTPUT_FILE)

main()
