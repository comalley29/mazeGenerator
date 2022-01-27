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


import cgi
import cgitb #found this but isn't used?

form = cgi.FieldStorage()







#if form.getvalue('styles') == "aldousbroder":
    #Mazestyle = "AldousBroder"

#if form.getvalue('styles') == "backtracking":
    #Mazestyle = "BacktrackingGenerator"

#print(Mazestyle)



m = Maze()
m.generator = Prims(27, 34)
m.generate()

#print(m.tostring())            # print walls only
#print(m.tostring(True))        # print walls and entrances
#print(m.tostring(True, True))  # print walls, entrances, and solution
#print(str(m))                  # print everything that is available
#print(m)    



import matplotlib.pyplot as plt

def showPNG(grid):
    """Generate a simple image of the maze."""
    plt.figure(figsize=(10, 5))
    plt.imshow(grid, cmap=plt.cm.binary, interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()
    x = plt

showPNG(m.grid)