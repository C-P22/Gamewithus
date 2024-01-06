import random
from icecream import ic
import sys

sys.setrecursionlimit(3000)


class Maze:
    WALL = "X"
    PATH = "."
    PLAYER = "P"
    VISITED = "V"  # is important for the maze generator so if a stone is the neighbor of two other stones make it a wall
    END = "E"

    def __init__(self, length, width, y_player, x_player):
        self.length = length
        self.width = width
        self.y_player = y_player
        self.x_player = x_player
        self.maze = [["u" for _ in range(self.length)] for _ in range(self.width)]
        self.visited = [[False for _ in range(self.length)] for _ in range(self.width)]

        self.dfs_search(self.y_player, self.x_player)
        self.maze[self.y_player][self.x_player] = Maze.PLAYER
        for y, blocks in enumerate(self.maze):
            for x, block in enumerate(blocks):
                if block == 'u':
                    self.maze[y][x] = "X"
        self.farthest_point()

    def farthest_point(self):
        start = [[self.y_player,self.x_player]]
        while len(start) > 0:

            y,x = start[0]
            if len(start) == 1:
                farthes_x = x
                farthes_y = y 
            self.visited[y][x] = True
            start.pop(0)
            neighbors = [[y - 1, x], [y + 1, x], [y, x + 1], [y, x - 1]]
            for neighbor in neighbors:
                y_neigbor,x_neigbor = neighbor
                if self.visited[y_neigbor][x_neigbor] == False and self.maze[y_neigbor][x_neigbor]== '.':
                    self.visited[y_neigbor][x_neigbor] = True
                    start.append([y_neigbor,x_neigbor])
        self.maze[farthes_y][farthes_x] = Maze.END
    
    def dfs_search(self, y, x):

        # ic(x, y, self.maze[y][x])
        self.maze[y][x] = Maze.PATH
        neighbors = [[y - 1, x], [y + 1, x], [y, x + 1], [y, x - 1]]
        for neighbor in neighbors:  # Iterate over a copy of the list
            y_now, x_now = neighbor
            if self.maze[y_now][x_now] == 'V':
                luck = 2
                if luck != 0:
                    self.maze[y_now][x_now] = Maze.WALL
            elif self.maze[y_now][x_now] == 'u':
                luck = 2
                if luck != 0:
                    self.maze[y_now][x_now] = Maze.VISITED
        # ic(neighbors)
        for i in range(4):
            choice = random.choice(neighbors)
            y_ne, x_ne = choice
            neighbors.remove(choice)
            if x_ne == 0 or x_ne == self.length - 1 or y_ne == 0 or y_ne == self.width - 1:
                self.maze[y_ne][x_ne] = Maze.WALL
            else:
                luck = random.randint(0, 30)  # jeder xte Block hat die Chance doch noch ein Path zu werden
                if self.maze[y_ne][x_ne] == 'u' or self.maze[y_ne][x_ne] == 'V' or luck == 0:
                    self.dfs_search(y_ne, x_ne)