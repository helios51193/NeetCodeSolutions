# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

# Morris in order traversal
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = root

    def next(self) -> int:
        # traverse while current
        while self.curr:
            # left is null, set current to right and return the value
            if not self.curr.left:
                val = self.curr.val
                self.curr = self.curr.right
                return val
            else:
                # got right till you right is not null or right is current
                pred = self.curr.left
                while pred.right and pred.right!=self.curr:
                    pred = pred.right
                # create a temporary thread and return the val
                if pred.right==self.curr:
                    pred.right=None
                    val = self.curr.val
                    self.curr= self.curr.right
                    return val
                # undo the thread
                else:
                    pred.right = self.curr
                    self.curr = self.curr.left

    def hasNext(self) -> bool:
        return self.curr is not None


"""
    Last Looked
    16-11-25

"""