from typing import Optional

# inorder traversal will give you sorted list
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        sorted_elements = inorder_traversal(root)
        return sorted_elements[k-1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = 0 
        self.k = k 
        self.inorder(root)
        return self.ans
    
    def inorder(self, node):
        if node.left:
            self.inorder(node.left)

        self.count += 1
        if self.count == self.k:
            self.ans = node.val
            return 
        
        if node.right:
            self.inorder(node.right)



"""
    Last Looked
    18-11-25

"""