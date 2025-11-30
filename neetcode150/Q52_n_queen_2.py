class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        colset = set()
        lud = set()
        rud = set()

        def backtrack(row):
            nonlocal res
            if row == n:
                # found the solution
                res += 1
                return 
            
            # traverse each col
            for col in range(n):
                # continue if the col and 2 diagonals are already occupied
                if col in colset or row-col in lud or row+col in rud:
                    continue
                
                # Add to the list of occupied column and diagnoals
                colset.add(col)
                lud.add(row-col)
                rud.add(row+col)

                backtrack(row+1)

                colset.remove(col)
                lud.remove(row-col)
                rud.remove(row+col)
            
        # traverse each row
        backtrack(0)
        return res

"""
    1. recurse using the row and keep check of colums and diagonals
    2. the above solution is slow as it is uses insertion and deletion from sets. It can be simplified by creating a nxn board and create a function called isSafe( check the below sol)
"""

"""
    Last Looked
    30-11-25

"""
"""
Alternate solution
class Solution:

    def isSafe(self, board, r,c,ans):
        for j in range(c):
            if board[r][j] == 'Q':
                return False
        for i in range(r):
            if board[i][c] == 'Q':
                return False
        i,j = r,c
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        i,j = r,c
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def nQueens(self, board, row, ans):
        if row == len(board):
            ans.append([''.join(r) for r in board])
            return
        
        for j in range(len(board)):
            if self.isSafe(board, row, j, ans):
                board[row][j] = 'Q'
                self.nQueens(board, row+1, ans)
                board[row][j] = '.'

    def totalNQueens(self, n: int) -> int:
        board = [['.' for j in range(n)] for i in range(n)]
        ans = []
        self.nQueens(board, 0, ans)
        return len(ans)
""" 