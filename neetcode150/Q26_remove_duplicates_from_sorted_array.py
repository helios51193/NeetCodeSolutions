# Solution 1
# Popping the duplicate element
from typing import List


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
# Solution 2
# Using set
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = sorted(set(nums))
        for i in range(len(x)):
            nums[i] = x[i]
        
        return len(x)