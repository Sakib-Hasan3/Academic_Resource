from collections import deque

def dfs(tree, start, visited=None):
    if visited is None:
        visited = []
    
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
        
        for node in tree[start]:
            dfs(tree, node, visited)
    
    return visited

# Example usage:
# Define a graph as an adjacency list
tree = {
        'A': ['B', 'E'],
        'B': ['C', 'D'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

# Call the DFS function
print("DFS traversal starting from 'A':")
result = dfs(tree, 'A')
print(f"\nVisited nodes: {result}")