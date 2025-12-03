

import sys


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        cur_sum = 0
        max_sum = -sys.maxsize - 1
        for i in range(n):
            cur_sum += nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        
        return max_sum


"""
    Last Looked
    03-11-25

"""