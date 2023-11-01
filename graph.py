class Graph:

  def __init__(self):
    self.num_nodes = 0
    self.num_edges = 0
    self.adj = {}

  def add_node(self, node):
    if node not in self.adj:
      self.adj[node] = {}
      self.num_nodes += 1
      
  def add_edge(self, u, v, weight):
    if u not in self.adj:
      self.add_node(u)
    if v not in self.adj:
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
    
  def degree_out(self, node):
    return len(self.adj[node])
  
  def degree_in(self, node):
    count = 0
    for key in self.adj:
      if node in self.adj[key]:
        count += 1
    return count  
  
  def neighbors(self, node):
    return list(self.adj[node].keys())

  def __repr__(self) -> str:
    str = ""
    for u in self.adj:
      str += f"{u} -> {self.adj[u]}\n"
    return str