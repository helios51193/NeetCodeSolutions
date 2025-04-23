from typing import List

# This is just a simulation of spiral traversal
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        top, bottom = 0, len(matrix) -1
        left, right = 0, len(matrix[0]) -1

        while top <= bottom and left <=right:

            # Top row
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            
            # Right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # bottom row
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -=1
            

            if left <=right:
                # left column
                for i in range(bottom, top-1,-1):
                    res.append(matrix[i][left])
                left += 1
        
        return res