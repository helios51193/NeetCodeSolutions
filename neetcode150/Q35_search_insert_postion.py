
# Basic binary search
import bisect


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        low, high = 0 , len(nums)

        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


# Using bisect
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return bisect.bisect_left(nums,target)
"""
    Last Looked
    03-12-25

"""