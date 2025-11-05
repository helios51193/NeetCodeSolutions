from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = curr = 0
        n = len(nums)
        minSize = n + 1
        for i in range(n):
            
            curr += nums[i] #expand the window
            #print(f"Expanding : {curr}")
            while curr >= target:
                minSize = min(minSize, i-start + 1) # update minsize
                curr -= nums[start] #shrink the window
                #print(f"Shrinking : {curr}  {i-start+1}")
                start += 1 
                
        
        return 0 if minSize > n else minSize

"""
    Last Looked
    5-11-25

"""