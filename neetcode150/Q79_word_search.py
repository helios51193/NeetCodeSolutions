class Solution:
    
    def backtracking(self, r, c, m, n, ind, board, word):

        # found the word
        if ind == len(word):
            return True
        
        # either outside the board or character not equal to currently traversed
        if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[ind]:
            return False
        
        temp = board[r][c]
        board[r][c] = '#'  # mark as visited
        down = self.backtracking(r + 1, c, m, n, ind + 1, board, word)
        if down:
            return True
        up = self.backtracking(r - 1, c, m, n, ind + 1, board, word)
        if up:
            return True
        left = self.backtracking(r, c - 1, m, n, ind + 1, board, word)
        if left:
            return True
        right = self.backtracking(r, c + 1, m, n, ind + 1, board, word)
        if right:
            return True
        
        board[r][c] = temp  # backtrack

        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.backtracking(i, j, m, n, 0, board, word):
                        return True
        return False


"""
    Last Looked
    30-11-25

"""

"""
Alternate 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        row = len(board)
        col = len(board[0])


        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            tmp = board[i][j]
            board[i][j] = "#"

            ok = (
                (i+1 < row and board[i+1][j] != "#" and dfs(i+1, j, k+1)) or
                (i-1 >= 0 and board[i-1][j] != "#" and dfs(i-1, j, k+1)) or
                (j+1 < col and board[i][j+1] != "#" and dfs(i, j+1, k+1)) or
                (j-1 >=0 and board[i][j-1] != "#" and dfs(i, j-1, k+1))
            )

            board[i][j] = tmp

            return ok

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True 
        return False
"""