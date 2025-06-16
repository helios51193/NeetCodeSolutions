# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr, val_sum):
            if not curr:
                return 0
            
            val_sum = val_sum * 10  + curr.val
            if not curr.left and not curr.right:
                return val_sum
            
            return dfs(curr.left, val_sum) + dfs(curr.right, val_sum)

        return dfs(root, 0)
