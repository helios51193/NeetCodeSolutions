# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = root.val

        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        if not node:
            return 0
        
        # Individually calculate left subtree and right subtree
        left_sum = max(0,self.dfs(node.left))
        right_sum = max(0, self.dfs(node.right))

        # Update the global max path, this is the case when the current node acts as a bridge
        # splitting into left and right
        # It is the highest sum encountered so far
        self.res = max(self.res, left_sum + right_sum + node.val)
        

        # Return the maximum without splitting
        # Either go left or right because valid path is a single path
        return max(left_sum, right_sum) + node.val


"""
    Last Looked
    16-11-25

"""