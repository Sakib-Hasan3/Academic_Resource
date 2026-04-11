from collections import deque 

def bfs(tree, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print(node, end=" ")
            
            for neighbour in tree[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    
    return visited

# Example usage:
# Define a graph as an adjacency list
tree = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Call the BFS function
print("BFS traversal starting from 'A':")
result = bfs(tree, 'A')
print(f"\nVisited nodes: {result}")
