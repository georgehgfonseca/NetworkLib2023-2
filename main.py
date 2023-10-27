from graph import Graph

g = Graph()
g.add_two_way_edge("Ana", "Bia", 1)
g.add_two_way_edge("Ana", "Caio", 1)
g.add_two_way_edge("Caio", "Bia", 1)
g.add_two_way_edge("Caio", "Duda", 1)
print(g)
print(g.there_is_edge("Ana", "Duda"))
print(g.degree_out("Ana"))
print(g.degree_in("Ana"))
print(g.neighbors("Ana"))