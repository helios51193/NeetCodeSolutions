# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        inorder_map = {val:index for index,val in enumerate(inorder)}

    
        def build_tree(pre_start, pre_end, in_start, in_end):

            if pre_start > pre_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            in_index = inorder_map[root_val]
            left_size = in_index - in_start

            root.left = build_tree(pre_start+1, pre_start + left_size, in_start, in_index-1)
            root.right = build_tree(pre_start + left_size + 1, pre_end, in_index + 1, in_end)

            return root

        return build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)

"""
    Last Looked
    15-11-25

"""