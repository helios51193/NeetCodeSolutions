import copy
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp = copy.deepcopy(board)

        m = len(board[0])
        n = len(board)
        # offsets for of 8 directions for neighbors
        moves = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]

        for i in range(n):
            for j in range(m):
                neighbors = 0
                # calculate number of neighbours
                for x,y in moves:
                    if (0 <= i+x < n) and (0 <= j+y < m):
                        if temp[i+x][j+y] == 1:
                            neighbors += 1
                
                # apply rules
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3: # rule 1 and 3
                        board[i][j] = 0
                    if neighbors == 2 or neighbors == 3: # rule 2
                        board[i][j] = 1
                
                if board[i][j] == 0:
                    if neighbors == 3:
                        board[i][j] = 1
        

        
        