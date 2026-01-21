from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        dfs1 = self.dfs(root1)
        dfs2 = self.dfs(root2)
        return dfs1 == dfs2

    def dfs(self, root):
        if root is None:
            return []

        leaves = self.dfs(root.left) + self.dfs(root.right)

        return leaves or [root.val]


"""
    Last Looked
    21-01-26

"""  