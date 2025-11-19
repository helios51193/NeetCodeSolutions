from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder(root,output):
            if root == None:
                return 
            else:
                inorder(root.left, output)
                output.append(root.val)
                inorder(root.right, output)
            
        output = []
        inorder(root,output)
        mini_diff = float('inf')
        for i in range(1,len(output)):
            mini_diff = min(mini_diff,output[i]-output[i-1])
        return mini_diff

# Definition for a binary tree node.
# in order traversal and maintain previous
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.prev = None
        self.res = float('inf')

        def dfs(node):
            if node:
                dfs(node.left)
                if self.prev is not None:
                    self.res = min(self.res, node.val - self.prev)

                self.prev = node.val
                dfs(node.right)
        
        dfs(root)
        return self.res


"""
    Last Looked
    18-11-25

"""