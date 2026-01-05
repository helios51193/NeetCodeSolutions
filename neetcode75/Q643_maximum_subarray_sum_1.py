class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        if k == 1:
            return max(nums)
        
        s = sum(nums[:k])
        m = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i-k]
            if s > m:
                m = s
        
        return m/float(k)