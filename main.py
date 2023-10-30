from graph import Graph

g = Graph()
g.add_two_way_edge("Ana", "Bia", 1)
g.add_two_way_edge("Ana", "Caio", 1)
g.add_two_way_edge("Caio", "Bia", 1)
g.add_two_way_edge("Caio", "Duda", 1)


g.printGraph()