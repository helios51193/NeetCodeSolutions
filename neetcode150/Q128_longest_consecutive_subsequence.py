from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        

        nums_set = set(nums)
        mx = 0
        for num in nums:
            if num-1 not in nums_set:
                tmp = 1
                while num+tmp in nums_set:
                    tmp +=1
                mx = max(mx,tmp)
        
        return mx

"""
    Last Looked
    10-11-25

"""