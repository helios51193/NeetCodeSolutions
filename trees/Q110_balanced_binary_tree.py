# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root:TreeNode):

            # check if empty node
            if root is None:
                return 0
            
            left = dfs(root.left) # Explore left subtree
            right = dfs(root.right) # Explore right subtree

            # Mark the unbalanced and propogate
            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1
            
            return max(left,right) + 1
        
        return dfs(root) != -1
        