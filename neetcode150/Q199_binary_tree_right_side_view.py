# Definition for a binary tree node.
from collections import deque
from typing import Optional

# same approach as Q117, at the end of each iteration the 
# prev pointer will be on the right most element of the current level
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        
        res = []
        q = deque()
        q.append(root)
        while q:
            right_side = None
            
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            
            if right_side:
                res.append(right_side.val)

        return res

"""
    Last Looked
    17-11-25

"""