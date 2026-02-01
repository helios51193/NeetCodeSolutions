from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)

        while q:
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                for key in rooms[cur]:
                    if key not in visited:
                        q.append(key)
                        visited.add(key)

        return len(visited) == len(rooms)
    

    
"""
    Last Looked
    01-02-26

"""