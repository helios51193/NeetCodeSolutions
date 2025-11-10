from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement_map = {n:index for index,n in enumerate(nums)}
        for index,nm in enumerate(nums):
           diff = target - nm
           if diff in complement_map.keys() and complement_map[diff] != index:
                return [index,complement_map[diff]]

"""
    Last Looked
    10-11-25

"""