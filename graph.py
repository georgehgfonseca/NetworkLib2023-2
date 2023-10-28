class Graph:

  def __init__(self):
    self.num_nodes = 0
    self.num_edges = 0
    self.adj = {}

  def add_node(self, node): #Reduzido de O(n) p/ O(1)
    try: 
      if self.adj[node] != {}:
        #print(f'Key {node} already exists and isnt null')
        return
    except KeyError:
      self.adj[node] = {}
      self.num_nodes += 1
      
  def add_edge(self, u, v, weight): #Reduzido de O(2n) p/ O(1)
    self.add_node(u)
    self.add_node(v)
    self.adj[u][v] = weight
    self.num_edges += 1

  def add_two_way_edge(self, u, v, weight):
    self.add_edge(u, v, weight)
    self.add_edge(v, u, weight)

  def printGraph(self):
    nodes = self.adj.items()
    for i, j in nodes:
      print(i, j)


