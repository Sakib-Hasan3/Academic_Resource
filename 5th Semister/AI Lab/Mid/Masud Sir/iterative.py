def dfs_limited(tree, start, limit, visited=None):
    if visited is None:
        visited = []
    
    if limit <= 0:
        return visited
    
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
        
        for node in tree[start]:
            dfs_limited(tree, node, limit-1, visited)
    
    return visited

def iterative_deepening(tree, start, max_limit):
    for i in range(max_limit):
        print(f"Iteration {i+1} : ", end="")
        dfs_limited(tree, start, i+1, [])
        print()

# Define a graph as an adjacency list
tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Call the Iterative Deepening function
print("Iterative Deepening Search starting from 'A' with max limit 4:")
iterative_deepening(tree, 'A', 4)
