# Definition for singly-linked list.
import heapq
from typing import Optional

# Using Heap
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        heap = []
        # Add the first value of each list to a heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i))
        
        # now whe we pop the heap, we will have the lowest value 
        while heap:
            # pop the heap and append to the dummy
            # now forward the the value of the list from which we we took the value
            # by .next  and add it to the heap
            val, i = heapq.heappop(heap)
            curr_node = lists[i]
            lists[i] = curr_node.next

            tail.next = curr_node
            tail = curr_node
            # We will always pull the lowest from the available values to check
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
            
        
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Using divide and conquere and recursion
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return self.divide_conquere(lists,0, len(lists) - 1)

    def divide_conquere(self, lists: list[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]

        mid = left + (right - left) // 2
        l1 = self.divide_conquere(lists, left, mid)
        l2 = self.divide_conquere(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


"""
    Last Looked
    03-11-25

"""