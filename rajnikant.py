
# Rajnikant Plane Survival

import random

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight=None) -> object:
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dfs_util(self, v, visited):
        visited.add(v)
        total_weight = 0

        for neighbor, weight in self.graph.get(v, []):
            if neighbor not in visited:
                print(" - Terrorist killed :", weight,"\nMoving To Plane :",neighbor)
                total_weight += weight
                total_weight += self.dfs_util(neighbor, visited)

        return total_weight

    def dfs(self, start):
        visited = set()
        total_weight = self.dfs_util(start, visited)
        print("\nAfter Police Declaration Total Terrorist Killed :", total_weight)


if __name__ == "__main__":
    graph = Graph()

    graph.add_edge(1, 2, random.randint(1, 5))
    graph.add_edge(1, 6, random.randint(1, 5))
    graph.add_edge(1, 7, random.randint(1, 5))
    graph.add_edge(2, 3, random.randint(1, 5))
    graph.add_edge(2, 4, random.randint(1, 5))
    graph.add_edge(2, 5, random.randint(1, 5))

    print("\nStarting from Plane : 1")
    graph.dfs(1)
        
