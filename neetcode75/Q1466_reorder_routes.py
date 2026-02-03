from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for u,v in connections:
            graph[v].append((u, 0))
            graph[u].append((v, 1)) 
            
        
        visited = set()
        def dfs(city):
            visited.add(city)
            changes = 0
            for nei, cost in graph[city]:
                if nei not in visited:
                    changes += cost
                    changes += dfs(nei)
            return changes

        return dfs(0)

"""
    Last Looked
    03-02-26

"""