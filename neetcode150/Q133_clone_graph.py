class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Maintain a hash table to check the already copied
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        self.copied = {}
        return self.dfs(node)
    
    def dfs(self, curr):
        if curr in self.copied:
            return self.copied[curr]
        clone = Node(curr.val, [])
        self.copied[curr] = clone

        for neighbor in curr.neighbors:
            clone_neighbors = self.dfs(neighbor)
            clone.neighbors.append(clone_neighbors)
        
        return clone