from Resources import config
import pygame
from pygame.locals import *
import sys


def index(grid, i, j, rows, cols):

    """ Returns the cell based on input
        Used in Gen.Evolve() """

    if i < 0 or j < 0 or i > cols - 1 or j > rows - 1:
        a = -1
    else:
        a = grid[i, j]
    return a


def breakWall(a, b):

    """ breaks the wall between a and b """

    temp = a.x - b.x
    if temp == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif temp == -1:
        a.walls[1] = False
        b.walls[3] = False

    bar = a.y - b.y
    if bar == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif bar == -1:
        a.walls[2] = False
        b.walls[0] = False


def drawMaze(arr, screen):

    """ Renders/Updates all the cells in the Array"""

    for row in range(config.rows):
        for col in range(config.cols):
            arr[row, col].render(screen)
    pygame.display.update()