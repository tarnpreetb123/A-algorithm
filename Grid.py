import Nodes
import math
import pygame

class Grid:

    def __init__(self, display):
        self.display = display
        self.done = False
        self.rows = 25
        self.cols = 40
        self.grid = [[Nodes.node(i, j, display) for j in range(self.cols)] for i in range(self.rows)]
        self.start = self.grid[10][20]
        self.end = self.grid[self.rows - 1][self.cols - 1]
        self.openSet = []
        self.closedSet = []
        self.path = []
        self.openSet.append(self.start)

        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j].add_neighbors(self.grid, self.rows, self.cols)

        self.start.wall = False
        self.end.wall = False

    def update(self):
        self.path = []

        best_index = 0

        # Find the node in the open set with the lowest f value
        for i in range(len(self.openSet)):
            if self.openSet[i].f < self.openSet[best_index].f:
                best_index = i

        # Calculate the path
        temp = self.openSet[best_index]
        while temp.previous:
            self.path.append(temp.previous)
            temp = temp.previous

        # If the node with the lowest f is the end then we are done
        if self.openSet[best_index] is self.end:
            self.done = True

        current = self.openSet[best_index]

        # Add the node with the lowest f to the closeSet and remove from the openSet
        self.closedSet.append(current)
        self.openSet.pop(best_index)

        # Loop through all the neighbours of current
        for i in range(len(current.neighbors)):
            neighbor = current.neighbors[i]

            # If the neighbour is not in the closed set update its g value
            if neighbor not in self.closedSet and not neighbor.wall:
                temptG = current.g + math.sqrt(pow(current.i - neighbor.i, 2) + pow(current.j - neighbor.j, 2))

                newPath = False

                if neighbor in self.openSet:
                    if temptG < neighbor.g:
                        neighbor.g = temptG
                        newPath = True
                else:
                    neighbor.g = temptG
                    self.openSet.append(neighbor)
                    newPath = True

                if newPath:
                    neighbor.h = self.heuristic(neighbor, self.end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current

    def heuristic(self, neighbor, end):
        distance = math.sqrt(pow(neighbor.i - end.i, 2) + pow(neighbor.j - end.j, 2))
        return distance

    def openSetNotEmpty(self):
        if len(self.openSet) > 0 and not self.done:
            return True
        else:
            return False

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j].draw()

        for i in range(len(self.openSet)):
            self.openSet[i].setColor((255, 0, 2))

        for i in range(len(self.closedSet)):
            self.closedSet[i].setColor((50, 50, 150))

        for i in range(len(self.path)):
            self.path[i].setColor((80, 255, 60))

    def update_mouse(self):

        i = math.floor(pygame.mouse.get_pos()[1] / self.grid[0][0].height)
        j = math.floor(pygame.mouse.get_pos()[0] / self.grid[0][0].width)

        if i < 0:
            i = 0
        if i > self.rows - 1:
            i = self.rows - 1
        if j < 0:
            j = 0
        if j > self.cols - 1:
            j = self.cols - 1

        #print(i)
        #print(pygame.mouse.get_pressed()[0])
        if pygame.mouse.get_pressed()[0] == 1:
            self.grid[i][j].set_wall(True)
        elif pygame.mouse.get_pressed()[2] == 1:
            self.grid[i][j].set_wall(False)



