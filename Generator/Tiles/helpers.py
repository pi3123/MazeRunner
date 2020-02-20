import numpy as np


def index(grid, i, j, rows, cols):
    if i < 0 or j < 0 or i > cols - 1 or j > rows - 1:
        a = -1
    else:
        a = grid[i, j]
    return a


def breakWall(a, b):
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
