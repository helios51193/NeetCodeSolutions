from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        n = len(isConnected)
        visited = [False] * n

        def run(start):
            queue = deque([start])
            visited[start] = True

            while queue:
                vertice = queue.popleft()
                for neigh in range(n):
                    if not visited[neigh] and isConnected[vertice][neigh] == 1:
                        visited[neigh] = True
                        queue.append(neigh)
        
        for i in range(n):
            if not visited[i]:
                province += 1
                run(i)
        
        return province

"""
    Last Looked
    02-02-26

"""