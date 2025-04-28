from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        subarrays = 0
        start = 0
        current_sum = 0
        for end, value in enumerate(nums):
            current_sum += value
            print(current_sum)
            while start <= end and current_sum * (end-start + 1) >= k:
                current_sum -= nums[start]
                start += 1
            
        
            subarrays += end-start + 1
        
        return subarrays