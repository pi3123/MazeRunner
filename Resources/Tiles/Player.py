import pygame

class Player:
    def __init__(self, grid, color=(0, 180, 0), x = 0, y = 0):
        self.grid = grid
        self.color = color
        self.W = grid[0, 0].W
        self.x = x
        self.y = y
        self.done = False
        self.reward = grid[self.x, self.y].reward

    def step(self, choice):

        """ Takes a step based on the input, if its possible(If there isn't a wall """

        if choice == 0:
            if self.possible(self.grid, choice):
                self.y -= 1
        elif choice == 1:
            if self.possible(self.grid, choice):
                self.x += 1
        elif choice == 2:
            if self.possible(self.grid, choice):
                self.y += 1
        elif choice == 3:
            if self.possible(self.grid, choice):
                self.x -= 1

        self.reward = self.grid[self.x, self.y].reward
        if self.reward == 1:
            self.done = True

        return (self.x, self.y), self.reward, self.done

    def render(self, screen):

        """ Draws that cell on the grid """

        pygame.draw.rect(
            screen,
            self.color,
            [self.x * self.W, self.y * self.W, self.W, self.W],
        )

    def possible(self, grid, choice):

        """ Checks if a move is possible (If there isn't a wall) """

        if not grid[self.x, self.y].walls[choice]:
            return True
        else:
            return False

    def __sub__(self, other):

        """ Subtraction overloading"""

        return other.x - self.x, other.y - self.y

