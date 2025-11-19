# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        self.p = p
        self.q = q
        
        return self.dfs(root)
        
    
    def dfs(self, node):
        if not node:
                return None
        if node.val == self.p.val or node.val == self.q.val:
            return node
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left and right:
            return node
        
        return left if left else right
    

"""
    Last Looked
    17-11-25

"""