# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        node1 = l1
        node2 = l2
        res_list = None
        curr = None
        carry = 0

        while node1 != None or node2 != None:
            
            op1 = 0
            op2 = 0
            if node1 != None:
                op1 = node1.val
                node1 = node1.next
            if node2 != None:
                op2 = node2.val
                node2 = node2.next

            res  = op1 + op2 + carry
            carry = res//10
            res  = res%10
            if res_list == None:
                res_list = ListNode(val=res)
                curr = res_list
            else:
                temp = ListNode(val=res)
                curr.next = temp
                curr = temp
        
        if carry !=0:
            res = carry
            temp = ListNode(val=res)
            curr.next = temp


        return res_list
            

        