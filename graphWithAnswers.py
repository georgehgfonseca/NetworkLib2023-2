class Graph:

  def __init__(self):
    self.num_nodes = 0
    self.num_edges = 0
    self.adj = {}

  def add_node(self, node):
    try: 
      if self.adj[node] != {}:
        return
    except KeyError:
      self.adj[node] = {}
      self.num_nodes += 1
      
  def add_nodes(self, nodes):
    for node in nodes:
      self.add_node(node)
      
  def add_edge(self, u, v, weight):
    self.add_node(u)
    self.add_node(v)
    self.adj[u][v] = weight
    self.num_edges += 1

  def add_two_way_edge(self, u, v, weight):
    self.add_edge(u, v, weight)
    self.add_edge(v, u, weight)

  def there_is_edge(self, u, v):
    try:
      self.adj[u][v]
      return True
    except KeyError:
      return False
    
  def neighbors(self, node):
    return list(self.adj[node].keys())

  def degree_out(self, node):
    return len(self.adj[node])
  
  def degree_in(self, node):
    count = 0
    for key in self.adj:
      if node in self.adj[key]:
        count += 1
    return count  

  def highest_degree_in(self):
    highest = 0
    for node in self.adj:
      degree_in_node = self.degree_in(node)
      if degree_in_node > highest:
        highest = degree_in_node
    return highest
  
  def density(self):
    return self.num_edges / (self.num_nodes * (self.num_nodes - 1))
  
  def is_regular(self):
    first_node = list(self.adj.keys())[0]
    degree_first_node = self.adj[first_node]
    for node in self.adj:
      if len(self.adj[node]) != degree_first_node:
        return False
      
  def is_oriented(self):
    for u in self.adj:
      for v in self.adj[u]:
        if not self.there_is_edge(v, u):
          return False
    return True

  def is_complete(self):
    return self.density() == 1
    

  def is_subgraph_of(self, g2):
    if self.num_nodes > g2.num_nodes or self.num_edges > g2.num_edges:
      return False
    for u in self.adj:
      for v in self.adj[u]:
        if not g2.there_is_edge(u, v):
          return False
    return True

  def strongest_connection(self):
    strongest = (None, None, float("-inf"))
    for u in self.adj:
      for v in self.adj[u]:
        if self.adj[u][v] > strongest[2]:
          strongest = (u, v, self.adj[u][v])
    return strongest
   
  def weakest_connection(self):
    weakest = (None, None, float("inf"))
    for u in self.adj:
      for v in self.adj[u]:
        if self.adj[u][v] < weakest[2]:
          weakest = (u, v, self.adj[u][v])
    return weakest

  def normalize_weights(self):
    highest_weight = self.strongest_connection()[2]
    smallest_weight = self.weakest_connection()[2]
    if highest_weight - smallest_weight == 0:
      print("WARN:  all weights are the same")
      return
    for u in self.adj:
      for v in self.adj[u]:
        self.adj[u][v] = (self.adj[u][v] - smallest_weight) / (highest_weight - smallest_weight)

  def bfs(self, s):
    pass

  def dfs(self, s):
    pass

  def dfs_rec(self, s):
    pass

  def __repr__(self) -> str:
    str = ""
    for u in self.adj:
      str += f"{u} -> {self.adj[u]}\n"
    return str

