from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
    
        slow, fast = head, head
        max_val = 0

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        curr, prev = slow, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev=  curr
            curr = nxt

        while prev:
            max_val = max(max_val, head.val + prev.val)
            prev = prev.next
            head = head.next
        
        return max_val

"""
    Last Looked
    21-01-26

"""  