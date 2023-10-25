##########################################################################################
# Graph representation as adjacency matrix
g = [[0, 1, 0, 1],
     [1, 0, 0, 1],
     [0, 0, 0, 1],
     [1, 1, 1, 0]]

# Check if there is edge from node 2 to node 3 (time complexity: O(1))
print(f"There is edge from {2} to {3}? {g[2][3]}")

# Print all neighbors of node 2
for j in range(len(g[2])):
  if g[2][j] == 1:
    print(f"Node 2 has neighbor {j}")

# If the graph is weighted, the adjacency matrix cells will store the weights
g = [[0, 5, 0, 4],
     [5, 0, 0, 1],
     [0, 0, 0, 2],
     [4, 1, 2, 0]]

# Main drawback: space complexity is O(n^2) even if the graph is sparse

##########################################################################################
# Graph representation as adjacency list
g = [[1, 3],
     [0, 3],
     [3],
     [0, 1, 2]]

# Check if there is edge from node 2 to node 3. Time complexity: O(n)
is_neighbor = False
for neighbor in g[2]:
  if neighbor == 3:
    is_neighbor = True
    break
print(f"There is edge from {2} to {3}? {is_neighbor}")

# Main drawback: search complexity is O(n) 

# It could be simpler using the in operator, although time complexity remains O(n)
print(f"There is edge from {2} to {3}? {3 in g[2]}")

# Print all neighbors of node 2
print(f"Node 2 has neighbors {g[2]}")

# If the graph is weighted, one solution is to store (neighbor, weight) pairs
g = [[(1, 5), (3, 4)],
     [(0, 5), (3, 1)],
     [(3, 2)],
     [(0, 4), (1, 1), (2, 2)]]

##########################################################################################
# What if nodes are not integers starting from 0? We can use dictionaries
g = { "Ana":  ["Bia", "Duda"],
      "Bia":  ["Ana", "Duda"],
      "Caio": ["Duda"],
      "Duda": ["Ana", "Bia", "Caio"] }

# Check if there is edge from node "Caio" to node "Duda"
print(f"There is edge from Caio to Duda? {'Duda' in g['Caio']}")

# What if the graph is weighted? We can use dictionaries of dictionaries
g = { "Ana":  {"Bia": 5, "Duda": 4},
      "Bia":  {"Ana": 5, "Duda": 1},
      "Caio": {"Duda": 2},
      "Duda": {"Ana": 4, "Bia": 1, "Caio": 2} }

# Check if there is edge from node "Caio" to node "Duda"
print(f"Edge from Caio to Duda has weight: {g['Caio']['Duda']}")

# Now check graph.py for object oriented implementation which we will use in the next classes