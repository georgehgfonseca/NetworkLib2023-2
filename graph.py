class Graph:

  def __init__(self):
    self.num_nodes = 0
    self.num_edges = 0
    self.adj = {}

  def add_node(self, node):
    if node not in self.adj:
      self.adj[node] = []
      self.num_nodes += 1
      