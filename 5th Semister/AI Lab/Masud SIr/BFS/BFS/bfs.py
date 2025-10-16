from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])   # queue stores paths, not just nodes
    
    while queue:
        path = queue.popleft()     # take the first path
        node = path[-1]            # last node in the path
        
        if node == goal:           # if goal found, return path
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None  # if no path found

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Find shortest path from A to F
print(bfs_shortest_path(graph, 'A', 'F'))


