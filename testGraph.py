import unittest
from graphWithAnswers import Graph

class TestExample(unittest.TestCase):
    
    def setUp(self):
        # create a few graphs
        self.g1 = Graph()
        self.g1.add_undirected_edge("Ana", "Bia", 1)
        self.g1.add_undirected_edge("Ana", "Caio", 1)
        self.g1.add_undirected_edge("Caio", "Bia", 1)
        self.g1.add_undirected_edge("Caio", "Duda", 1)


    def tearDown(self):
        # Code to run after each test method
        pass

    def test_neighboring(self):
          self.assertEqual(self.g1.neighbors("Ana"), ["Bia", "Caio"])
          self.assertEqual(self.g1.degree_out("Ana"), 2)
          self.assertEqual(self.g1.degree_in("Ana"), 2)
          self.assertEqual(self.g1.highest_degree_in(), 3)
          self.assertEqual(self.g1.density(), 2/3)
