from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        reverse = False
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
            
            if len(temp) > 0:
                res.append(temp if not reverse else temp[::-1])
                reverse = not reverse

        return res