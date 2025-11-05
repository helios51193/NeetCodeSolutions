from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set) # rows
        cols = defaultdict(set) # coumns
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


"""
    Last Looked
    5-11-25

"""