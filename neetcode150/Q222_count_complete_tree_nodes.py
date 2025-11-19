from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.get_depth_left(root.left)
        right = self.get_depth_right(root.right)

        
        # If left sub tree height equals right sub tree height then,
        #       a. left sub tree is perfect binary tree
        #       b. right sub tree is complete binary tree
        # If left sub tree height greater than right sub tree height then,
        #       a. left sub tree is complete binary tree
        #       b. right sub tree is perfect binary tree
        if left == right:
            return (1 << (left + 1)) - 1     
        
        return 1 + self.countNodes(root.left)  + self.countNodes(root.right)
            
    
    def get_depth_left(self,node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d

    def get_depth_right(self, node):
        d = 0
        while node:
            d +=1
            node = node.right
        return d


"""
    Last Looked
    17-11-25

"""