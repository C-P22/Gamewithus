import random 
from icecream import ic 
class Maze:
    WALL = "X"
    PATH = "."
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.maze=[["u" for _ in range(self.length)] for _ in range(self.width)]
    def get_start(self):
       # ic(self.length/2,self.width/2)

        self.maze[self.width//2][0] = Maze.PATH


g = Maze(30,20)
g.get_start()
print(g.maze)    