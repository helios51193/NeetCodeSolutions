from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance[0],entrance[1], 0))
        # mark the starting as traversed
        maze[entrance[0]][entrance[1]] = "+"

        while queue:
            row, col, steps = queue.popleft()

            for dx,dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dy, col + dx
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                    if (nr == 0 or nr == m - 1) or (nc == 0 or nc == n - 1):
                        return steps + 1 # the solution
                    
                    maze[nr][nc] = "+"
                    queue.append((nr, nc, steps + 1))

        return -1

"""
    Last Looked
    06-02-26

"""