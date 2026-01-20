# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head

        odd, even = ListNode(0), ListNode(0)
        odd_ptr, even_ptr = odd, even
        is_odd = True
        while head != None:
            if not is_odd:
                even_ptr.next = head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next

            head = head.next
            is_odd = not is_odd

        even_ptr.next = None
        odd_ptr.next = even.next

        return odd.next

"""
    Last Looked
    20-01-26

"""  