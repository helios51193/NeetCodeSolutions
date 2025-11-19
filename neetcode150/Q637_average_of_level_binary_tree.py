from collections import deque
from typing import Optional

# same approach as Q117
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        
        res = []
        q = deque()
        q.append(root)
        while q:
            right_side = None
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    right_side = node
                    temp.append(right_side.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if n := len(temp) > 0:
                res.append(sum(temp)/len(temp))

        return res

"""
    Last Looked
    17-11-25

"""