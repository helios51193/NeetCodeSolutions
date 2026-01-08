
# Specific case of Q1004
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        if 0 not in nums:
            return len(nums) - 1

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left)
        return max_len