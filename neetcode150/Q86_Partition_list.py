# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_start, right_start = ListNode(0, None), ListNode(0,None)
        curr_left, curr_right = left_start, right_start

        curr = head
        while curr:
            if curr.val < x:
                curr_left.next = ListNode(curr.val, None)
                curr_left = curr_left.next
            else:
                curr_right.next = ListNode(curr.val, None)
                curr_right = curr_right.next
            curr = curr.next
        
        curr_left.next = right_start.next
        return left_start.next