# Definition for a binary tree node.
from typing import List, Optional

# similar to Q105
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        rec = {val:i for i , val in enumerate(inorder)}

        def build_tree(in_start, in_end, post_start, post_end):

            if in_start > in_end or post_start > post_end:
                return None
            

            val = postorder[post_end]
            root = TreeNode(val)
            idx = rec[val]
            left_subtree_size = idx - in_start
            root.left = build_tree(in_start, idx-1, post_start, post_start + left_subtree_size-1)
            root.right = build_tree(idx+1,in_end, post_start+left_subtree_size, post_end-1 )

            return root
        
        return build_tree(0, len(inorder)-1, 0, len(postorder)-1)