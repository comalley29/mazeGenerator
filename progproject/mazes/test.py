from re import A
from mazelib import Maze
from mazelib.generate.Prims import Prims
from mazelib.mazelib import Maze
from mazelib.generate.AldousBroder import AldousBroder
from mazelib.generate.BacktrackingGenerator import BacktrackingGenerator
from mazelib.generate.BinaryTree import BinaryTree
from mazelib.generate.CellularAutomaton import CellularAutomaton
from mazelib.generate.Division import Division
from mazelib.generate.DungeonRooms import DungeonRooms
from mazelib.generate.Ellers import Ellers
from mazelib.generate.GrowingTree import GrowingTree
from mazelib.generate.HuntAndKill import HuntAndKill
from mazelib.generate.Kruskal import Kruskal
from mazelib.generate.Prims import Prims
from mazelib.generate.Sidewinder import Sidewinder
from mazelib.generate.TrivialMaze import TrivialMaze
from mazelib.generate.Wilsons import Wilsons
import django
from django.conf import settings
import cgi
import matplotlib.pyplot as plt


#print(m.tostring())            # print walls only
#print(m.tostring(True))        # print walls and entrances
#print(m.tostring(True, True))  # print walls, entrances, and solution
#print(str(m))                  # print everything that is available
#print(m)    



def showPNG(grid):
    """Generate a simple image of the maze."""
    plt.figure(figsize=(10, 5))
    plt.imshow(grid, cmap=plt.cm.binary, interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()
    x = plt

#m = Maze()
#m.generator = Prims(int(height), int(width))
#m.generate()
#showPNG(m.grid)

m = Maze()
m.generator = Prims(20, 20)
m.generate()
showPNG(m.grid)



def makeMaze(height, width, func):
    if func == Prims:
        m = Maze()
        m.generator = Prims(int(height), int(width))
        m.generate()
        showPNG(m.grid)
