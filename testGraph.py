# Teste de software
# Teste unitario (testes automatizados)
# Teste de integração
# ...
# TDD


import unittest
from graphWithAnswers import Graph
import time
class TestGraph(unittest.TestCase):
    
    def setUp(self):
        # create a few graphs
        self.g1 = Graph()
        self.g1.add_undirected_edge("Ana", "Bia", 1)
        self.g1.add_undirected_edge("Ana", "Caio", 1)
        self.g1.add_undirected_edge("Caio", "Bia", 1)
        self.g1.add_undirected_edge("Caio", "Duda", 1)

        self.got = Graph()
        self.got.add_undirected_edge("H", "K", 8)
        self.got.add_undirected_edge("H", "R", 10)
        self.got.add_undirected_edge("H", "P", 14)
        self.got.add_undirected_edge("K", "R", 25)
        self.got.add_undirected_edge("K", "T", 5)
        self.got.add_undirected_edge("R", "T", 2)
        self.got.add_undirected_edge("R", "P", 3)
        self.got.add_undirected_edge("P", "W", 18)
        self.got.add_undirected_edge("T", "W", 10)


    def tearDown(self):
        # Code to run after each test method
        pass

    def test_neighboring(self):
          self.assertEqual(self.g1.neighbors("Ana"), ["Bia", "Caio"])
          self.assertEqual(self.g1.degree_out("Ana"), 2)
          self.assertEqual(self.g1.degree_in("Ana"), 2)
          self.assertEqual(self.g1.highest_degree_in(), 3)
          self.assertEqual(self.g1.density(), 2/3)

    def test_shotest_path(self):
        got_shotest_path_output = ({"H": 0, "K": 8, "P": 13, "R": 10, "T": 12, "W": 22}, 
             {"H": None, "K": "H", "R": "H", "P": "R", "T": "R", "W": "T"})

        self.assertEqual(self.got.dijkstra_naive("H"), got_shotest_path_output)
        self.assertEqual(self.got.dijkstra("H"), got_shotest_path_output)
        self.assertEqual(self.got.bellman_ford_naive("H"), got_shotest_path_output)
        self.assertEqual(self.got.bellman_ford("H"), got_shotest_path_output)

    def test_file_reading(self):
        g = Graph()
        g.read_from_file("datasets/toy.txt")
        self.assertEqual(g.num_nodes, 4)
        self.assertEqual(g.num_edges, 5)

    def test_runtimes(self):
        g = Graph()
        g.read_from_file("datasets/USA-road-dt.DC.txt")
        start_time = time.time()
        g.dijkstra(0)
        print("Dijkstra:", time.time() - start_time)

        start_time = time.time()
        g.dijkstra_naive(0)
        print("Naive Dijkstra:", time.time() - start_time)

        start_time = time.time()
        g.bellman_ford(0)
        print("BF:", time.time() - start_time)

        start_time = time.time()
        g.bellman_ford_naive(0)
        print("Naive BF:", time.time() - start_time)

