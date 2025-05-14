# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        count = 0
        while current:
            count += 1
            current = current.next
        
        while count >= k:
            current = prev.next
            nxt = current.next

            for _ in range(1,k):
                current.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = current.next

            prev = current
            count -=k
        
        return  dummy.next