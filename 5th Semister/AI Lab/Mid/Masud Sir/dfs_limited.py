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

# Define a graph as an adjacency list
tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Call the DFS Limited function
print("DFS Limited traversal starting from 'A' with limit 3:")
result = dfs_limited(tree, 'A', 3)
print(f"\nVisited nodes: {result}")
