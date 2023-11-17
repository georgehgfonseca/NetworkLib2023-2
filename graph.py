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
    pass
  
  def is_regular(self):
    pass

  def is_complete(self):
    pass

  def is_subgraph_of(self, g2):
    pass

  def strongest_connection(self):
    pass
   
  def weakest_connection(self):
    pass

  def normalize_weights(self):
    pass

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

