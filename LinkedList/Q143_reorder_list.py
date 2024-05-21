# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # get the center of the list to divide the list into two parts
        cur = head
        slow, fast = cur,cur.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the links of the second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev =second
            second = tmp

        # merge both halves
        first, second = head, prev
        while first and second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first,second = t1, t2