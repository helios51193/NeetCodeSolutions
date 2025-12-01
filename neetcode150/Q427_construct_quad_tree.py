"""
# Definition for a QuadTree node.

"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        
        def dfs(x=0, y=0, n=len(grid)):
            
            if all(grid[x+i][y+j] == grid[x][y] for i in range(n) for j in range(n)): # check if all are equal within a quad
                return Node(grid[x][y] == 1, True)
            
            n//=2
            return Node(False, False, dfs(x,y,n), dfs(x,y+n,n) ,dfs(x+n,y,n), dfs(x+n,y+n,n)) #recurse over the 4 parts
        
        return dfs()
    

"""
    Last Looked
    01-12-25

"""