from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # check and store the status whether first row or column has zero or not
        firstRowZero = any(matrix[0][j] == 0 for j in range(n))
        firstColZero = any(matrix[i][0] == 0 for i in range(m))

        # Mark the row and columns as zero in the first column
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        

        # set zero based on marker
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        

        # Zero the first col and row if required 
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
        
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0

        