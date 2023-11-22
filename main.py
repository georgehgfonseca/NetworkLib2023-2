from copy import deepcopy
from graphWithAnswers import Graph
# from graph import Graph

# Lesson 1 - Graph representation and creation
g = Graph()
g.add_undirected_edge("Ana", "Bia", 5)
g.add_undirected_edge("Ana", "Caio", 2)
g.add_undirected_edge("Caio", "Bia", 10)
g.add_undirected_edge("Caio", "Duda", 7)
print(g)
print()

# Lesson 2 - Neighbors, degrees and density
print(f"Neighbors of Ana:", g.neighbors("Ana"))
print("Degree out of Ana:", g.degree_out("Ana"))
print("Degree in of Ana:", g.degree_in("Ana"))
print("Highest degree in:", g.highest_degree_in())
print("Density:", g.density())
print()

# Lesson 3 - Graph properties
print("Is regular:", g.is_regular())
print("Is complete:", g.is_complete())
print("Is oriented:", g.is_oriented())
g2 = Graph()
g.add_undirected_edge("Ana", "Bia", 5)
g.add_undirected_edge("Ana", "Caio", 2)
print("Is subgraph of g2:", g.is_subgraph_of(g2))
print("Strongest connection:", g.strongest_connection())
print("Weakest connection:", g.weakest_connection())
g2 = deepcopy(g)
g2.normalize_weights()
print(f"Graph with normalized weights:\n{g2}")
print()

# Lesson 4 - Graph traversal (BFS and DFS)
g = Graph()
g.add_nodes([0, 1, 2, 3, 4, 5, 6])
g.add_undirected_edge(0, 2, 1)
g.add_undirected_edge(0, 6, 1)
g.add_undirected_edge(1, 4, 1)
g.add_undirected_edge(1, 6, 1)
g.add_undirected_edge(2, 3, 1)
g.add_undirected_edge(2, 4, 1)
print("BFS from 0:", g.bfs(0))
print("DFS from 0:", g.dfs(0))
print("Recursive DFS from 0:", g.dfs_rec(0))
print()

# Lesson 5 - Exercises
