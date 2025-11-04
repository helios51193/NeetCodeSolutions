from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0 # Track of how farther we can go
        n = len(nums)
        for i in range(n):
            if i > farthest: # If i bigger that how farther we can go, it means we cannot reach the end
                return False
            farthest = max(farthest, i + nums[i])   # Take the max of current farthest and the traverse distance from current to the steps

        return True

"""
    Last Looked
    1-11-25

"""