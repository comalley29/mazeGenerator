from mazelib.generate.Prims import Prims
from mazelib.transmute.Perturbation import Perturbation
from mazelib import Maze

m = Maze()
m.generator = Prims(5, 5)
m.generate()
m.transmute()
m.start = (1, 0)
m.end = (5, 5)

