# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ahead = head

        # assign ahead to the nth element
        # return next if the list is smaller than n
        for i in range(n):
            if ahead.next:
                ahead = ahead.next 
            else:
                return head.next
        
        
        # ahead and follower are such that they are exactly n distance
        # away from each other.Keep going next with both until ahead is null
        # the the follower will be exactly at the n+1th element from the end
        follower = head
        while True:
            if ahead.next:
                ahead = ahead.next
                follower = follower.next
            else:
                follower.next = follower.next.next
                return head