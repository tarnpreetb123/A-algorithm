import pygame
import random

class node:

    def __init__(self, i, j, display):
        self.display = display
        self.previous = None
        self.i = i
        self.j = j
        self.width = 25
        self.height = 25
        self.wall = False
        self.color = (0, 0, 0)
        self.white = (255, 255, 255)

        #if random.randint(0, 100) < 30:
            #self.wall = True
            #self.color = (255, 211, 25)

        # Data for A* algorithm
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []

    def add_neighbors(self, grid, rows, cols):
        i = self.i
        j = self.j

        if i < rows - 1:
            self.neighbors.append(grid[i + 1][j])
            if j < cols - 1:
                self.neighbors.append(grid[i + 1][j + 1])
            if j > 0:
                self.neighbors.append(grid[i + 1][j - 1])
        if i > 0:
            self.neighbors.append(grid[i - 1][j])
            if j < cols - 1:
                self.neighbors.append(grid[i - 1][j + 1])
            if j > 0:
                self.neighbors.append(grid[i - 1][j - 1])
        if j < cols - 1:
            self.neighbors.append(grid[i][j + 1])
        if j > 0:
            self.neighbors.append(grid[i][j - 1])

    def setColor(self, color):
        self.color = color

    def set_wall(self, wall):
        self.wall = wall
        if wall:
            self.color = (255, 211, 25)
        else:
            self.color = (0, 0, 0)

    def draw(self):
        pygame.draw.rect(self.display, self.color, pygame.Rect(self.j * self.width, self.i * self.height, self.width, self.height))
        pygame.draw.rect(self.display, self.white, pygame.Rect(self.j * self.width, self.i * self.height, self.width, self.height), 1)
