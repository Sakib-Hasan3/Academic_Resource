from collections import deque

# Undirected Tree
un_tree = {
    'A': ['B', 'E'],
    'B': ['C', 'D', 'A'],
    'C': ['F', 'B'],
    'D': ['B'],
    'E': ['A'],
    'F': ['C']
}

def bidirectional(tree, start, goal):
    if start == goal:
        return [start], [goal]

    start_visited = []
    goal_visited = []

    start_queue = deque([start])
    goal_queue = deque([goal])

    while start_queue and goal_queue:
        # Forward search from start
        if start_queue:
            start_node = start_queue.popleft()
            if start_node not in start_visited:
                start_visited.append(start_node)
                print(f"Forward: {start_node}")

                for neighbour in tree[start_node]:
                    if neighbour not in start_visited:
                        start_queue.append(neighbour)

        # Backward search from goal
        if goal_queue:
            goal_node = goal_queue.popleft()
            if goal_node not in goal_visited:
                goal_visited.append(goal_node)
                print(f"Backward: {goal_node}")

                for neighbour in tree[goal_node]:
                    if neighbour not in goal_visited:
                        goal_queue.append(neighbour)

        # Check for intersection
        intersection = set(start_visited) & set(goal_visited)
        if intersection:
            print(f"Intersection found: {intersection}")
            return start_visited, goal_visited

    return start_visited, goal_visited

# Call the Bidirectional Search function
print("Bidirectional Search from 'A' to 'F':")
start_path, goal_path = bidirectional(un_tree, 'A', 'F')
print(f"\nStart visited: {start_path}")
print(f"Goal visited: {goal_path}")
