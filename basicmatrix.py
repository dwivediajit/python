import numpy as np

# Generate random 5x5 matrix
matrix = np.random.randint(1, 10, size=(5, 5))
print("Matrix with random terrorists:")
print(matrix)

# Dijkstra's Algorithm for Shortest Path
def dijkstra(matrix, start):
    num_vertices = len(matrix)
    visited = [False] * num_vertices
    distance = [float('inf')] * num_vertices
    distance[start] = 0

    for _ in range(num_vertices):
        min_dist = float('inf')
        min_index = -1
        for v in range(num_vertices):
            if not visited[v] and distance[v] < min_dist:
                min_dist = distance[v]
                min_index = v
        visited[min_index] = True
        for v in range(num_vertices):
            if not visited[v] and matrix[min_index, v] != 0 and distance[min_index] + matrix[min_index, v] < distance[v]:
                distance[v] = distance[min_index] + matrix[min_index, v]
    return distance

# Find the shortest path using Dijkstra's algorithm
shortest_path_distances = dijkstra(matrix, 0)

# Initialize a 5x5 memoization table with large values
memo = np.full((5, 5), np.inf)

# Store the damage of all paths
damage_grid = np.zeros((5, 5))
for i in range(5):
    for j in range(5):
        damage_grid[i, j] = matrix[i, j] + shortest_path_distances[i] - shortest_path_distances[j]

# Print the damage of all paths
print("\nDamage of all paths:")
for i in range(5):
    for j in range(5):
        print(f"From (0, 0) to ({i}, {j}): {damage_grid[i, j]}")

# Set the start point
memo[0, 0] = matrix[0, 0]

# Set the end point (desired indices) as 0
end_indices = [(0, 0)]  # Indices where you want the cost to be 0
for idx in end_indices:
    memo[idx] = 0

# Function to update memoization table with minimum damage
def update_memo(x, y):
    directions = [(1, 0), (0, 1), (1, 1)]  # right, down, and diagonal
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 5 and 0 <= new_y < 5:
            memo[new_x, new_y] = min(memo[new_x, new_y], memo[x, y] + matrix[new_x, new_y])

# Update memoization table
for i in range(5):
    for j in range(5):
        update_memo(i, j)

# Find the optimal path
path = [(4, 4)]  # start from home
x, y = 4, 4
while (x, y) != (0, 0):
    min_neighbor = min((memo[x + dx, y + dy], (dx, dy)) for dx, dy in [(0, -1), (-1, 0), (-1, -1)])
    dx, dy = min_neighbor[1]
    x, y = x + dx, y + dy
    path.append((x, y))

# Reverse the path to get it from start to home
path.reverse()

# Print the optimal path
print("\nOptimal path for soldier to traverse:")
for position in path:
    print(position)

# Print the total damage along the optimal path
print("\nTotal Damage from Terrorists along the optimal path:", memo[4, 4])
