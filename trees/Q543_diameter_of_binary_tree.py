# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.maxDiameter(root)
        return self.max_diameter
    
    def maxDiameter(self,  node: Optional[TreeNode]):

        if not (node.left or node.right):
            return 0
        
        leftMax = 1 + self.maxDiameter(node.left) if node.left else 0
        rightMax = 1 + self.maxDiameter(node.right) if node.right else 0

        self.max_diameter = max(self.max_diameter, leftMax + rightMax)

        return max(leftMax, rightMax)