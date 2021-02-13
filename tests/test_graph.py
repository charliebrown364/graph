import sys
sys.path.append('src')
from graph import Graph

edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
graph = Graph(edges)

assert graph.calc_distance(0,4) == 2
assert graph.calc_distance(5,2) == 3
assert graph.calc_distance(0,5) == 3
assert graph.calc_distance(4,1) == 1
assert graph.calc_distance(3,3) == 0

print("passed calc_distance tests")

assert graph.calc_shortest_path(0,4) == [0, 1, 4], graph.calc_shortest_path(0,4)
assert graph.calc_shortest_path(5,2) == [5, 4, 1, 2]
assert graph.calc_shortest_path(0,5) == [0, 1, 4, 5]
assert graph.calc_shortest_path(4,1) == [4, 1]
assert graph.calc_shortest_path(3,3) == [3]

print("passed calc_shortest_path tests")