# Solution - 1
# Using arrays and iterating over board 3 times
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        # function to check if the values are valid
        # A list of value are valid if numbers are not repeating
        def is_valid(values):
            arr = [x for x in values if x != '.']
            return len(arr) == len(set(arr))
        
        # check if all rows are valid
        for row in board:
            if not is_valid(row):
                return False
        
        # check for all columns:
        for col in zip(*board):
            if not is_valid(col):
                return False
        
        # check all 3x3 grids
        for i in (0,3,6):
            for j in (0,3,6):
                board3x3 = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not is_valid(board3x3):
                    return False
        
        return True

# Solution - 2
# using hashmaps
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set) 
        squares = defaultdict(set) # key( r/3,c/3) r= (0,3,6) , c = (0,3,6)

        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] == ".":
                    continue
                
                ele = board[row_idx][col_idx]
                if ele in rows[row_idx] or ele in cols[col_idx] or ele in squares[(row_idx//3,col_idx//3)]:
                    return False

                cols[col_idx].add(ele)
                rows[row_idx].add(ele)
                squares[(row_idx//3, col_idx//3)].add(ele)

        return True      