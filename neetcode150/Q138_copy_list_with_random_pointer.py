"""
# Definition for a Node.
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        # Create a hashmap with node -> new node with val
        old_new_map = {}
        
        curr = head
        while curr:
            old_new_map[curr] = Node(curr.val)
            curr = curr.next
        
        # Populate the next and random of new nodes based on map
        curr = head
        while curr:
            old_new_map[curr].next = old_new_map.get(curr.next)
            old_new_map[curr].random = old_new_map.get(curr.random)
            curr = curr.next
        
        return old_new_map[head]

"""
    Last Looked
    11-11-25

"""