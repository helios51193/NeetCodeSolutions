from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, max_reach, steps = 0,0,0

        for i in range(len(nums)-1):
            max_reach = max(max_reach, i + nums[i]) # Maintain the maximum range at each step that we can traverse
            if i == steps: # when we reach step ,increment the jump and update the steps which is the max reach
                jumps += 1
                steps = max_reach
        
        return jumps
    
"""
    Last Looked
    1-11-25

"""