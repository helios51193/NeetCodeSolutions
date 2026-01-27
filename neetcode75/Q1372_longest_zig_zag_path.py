# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, True, 0)
        return self.res
    
    def dfs(self, node, go_left, length):

        if not node:
            return 
        
        self.res = max(self.res, length)

        if go_left:
            self.dfs(node.left, False, length + 1)
            self.dfs(node.right, True, 1)
        else:
            self.dfs(node.right, True, length + 1)
            self.dfs(node.left, False, 1)
        