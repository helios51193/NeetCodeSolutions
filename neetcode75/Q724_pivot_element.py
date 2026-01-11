class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        
        left_sum, right_sum = 0, sum(nums)

        for idx,x in enumerate(nums):
            right_sum -= x
            if left_sum == right_sum:
                return idx
            
            left_sum += x
        
        return -1


"""
    Last Looked
    11-01-26

"""  