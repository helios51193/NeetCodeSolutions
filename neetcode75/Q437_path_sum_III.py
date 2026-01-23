# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.prefix_sum_count = defaultdict(int)
        self.prefix_sum_count[0] = 1
        self.target_sum = targetSum
        return self.dfs(root,0)
    
    def dfs(self, node, current_sum):
        if not node:
            return 0
        
        current_sum += node.val
        count = self.prefix_sum_count[current_sum -  self.target_sum]

        self.prefix_sum_count[current_sum] += 1

        count += self.dfs(node.left, current_sum) + self.dfs(node.right, current_sum)
        
        self.prefix_sum_count[current_sum] -= 1

        print(self.prefix_sum_count)

        if self.prefix_sum_count[current_sum] == 0:
            del self.prefix_sum_count[current_sum]
        
        return count