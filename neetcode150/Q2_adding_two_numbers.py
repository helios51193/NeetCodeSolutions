# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        curr = head
        carry = 0
        while l1 or l2 or carry:
            sm = carry
            if l1:
                sm += l1.val
                l1 = l1.next
            if l2:
                sm += l2.val
                l2 = l2.next

            carry = sm //10
            curr.next = ListNode(sm%10)
            curr = curr.next

        return head.next 