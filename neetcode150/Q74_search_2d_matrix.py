class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols -1

        while left <= right:
            mid = (left+right)//2
            mid_ele = matrix[mid//cols][mid%cols]
            if mid_ele < target:
                left = mid + 1
            elif mid_ele > target:
                right = mid -1
            else:
                return True
        
        return False

"""
    Last Looked
    03-12-25

"""