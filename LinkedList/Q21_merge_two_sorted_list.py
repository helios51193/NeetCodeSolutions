# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        start = None
        nxt = None
        s1,s2 = list1,list2
        while s1 != None or s2 != None:
            temp = ListNode()
            # if first list is exausted 
            if s1 == None:
                temp.val = s2.val
                s2 = s2.next
            # if second list is exausted
            elif s2 == None:
                temp.val = s1.val
                s1 = s1.next
            # if first list has smaller value than second
            elif s1.val < s2.val:
                temp.val = s1.val
                s1 = s1.next
            else:
                temp.val = s2.val
                s2 = s2.next
            
            if start == None:
                start = nxt = temp
            else:
                nxt.next = temp
                nxt = temp
        
        return start
            