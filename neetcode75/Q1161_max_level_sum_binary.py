# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])   
        level = 1

        max_val = None
        max_level = None
        while queue:

            total = 0
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                total += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            
            if max_val == None:
                max_val, max_level = total, level
            elif total > max_val:
                max_val, max_level = total, level
            
            level += 1
        
        return max_level

"""
    Last Looked
    28-01-26
"""