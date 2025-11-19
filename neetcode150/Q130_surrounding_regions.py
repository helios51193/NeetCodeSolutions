# special case of Q200
# filling only a specific set of positions which are joining the edge
# rest converted to x
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rows, self.cols  = len(board), len(board[0])

        for j in range(self.cols):
            # top row
            if self.board[0][j] == 'O':
                self.dfs(0, j)
            # bottom row
            if self.board[self.rows - 1][j] == 'O':
                self.dfs(self.rows - 1, j)

        for i in range(self.rows):
            # left col
            if self.board[i][0] == 'O':
                self.dfs(i, 0)
            # right col
            if self.board[i][self.cols - 1] == 'O':
                self.dfs(i, self.cols - 1)
        
        # Update the markers
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                elif self.board[i][j] == 'T':
                    self.board[i][j] = 'O'
                


    def dfs(self, r,c):
        if r < 0 or c < 0 or r >= self.rows or c >= self.cols or self.board[r][c] != 'O':
            return
        self.board[r][c] = 'T'

        self.dfs(r + 1, c)
        self.dfs(r - 1, c)
        self.dfs(r, c + 1)
        self.dfs(r, c - 1)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rows, self.cols  = len(board), len(board[0])

        for j in range(self.cols):
            # top row
            if self.board[0][j] == 'O':
                self.dfs(0, j)
            # bottom row
            if self.board[self.rows - 1][j] == 'O':
                self.dfs(self.rows - 1, j)

        for i in range(self.rows):
            # left col
            if self.board[i][0] == 'O':
                self.dfs(i, 0)
            # right col
            if self.board[i][self.cols - 1] == 'O':
                self.dfs(i, self.cols - 1)
        
        # Update the markers
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                elif self.board[i][j] == 'T':
                    self.board[i][j] = 'O'
                


    def dfs(self, r,c):
        if r < 0 or c < 0 or r >= self.rows or c >= self.cols or self.board[r][c] != 'O':
            return
        self.board[r][c] = 'T'

        self.dfs(r + 1, c)
        self.dfs(r - 1, c)
        self.dfs(r, c + 1)
        self.dfs(r, c - 1)
    

"""
    Last Looked
    19-11-25

"""

        
    



        