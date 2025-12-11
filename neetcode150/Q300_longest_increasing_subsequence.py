
# basic solution
import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] =  max(dp[i], dp[j] + 1)

        return max(dp)

# Greedy solution + binary search
class Solution:
    def lengthOfLIS(self, nums):
        tails = []  # tails[i] = smallest tail of all subseq of length i+1
        
        for num in nums:
            # Binary search: find leftmost position where num fits
            x = bisect.bisect_left(tails, num)
            
            if x == len(tails):
                # num is larger than all elements in tails
                # Extend the longest subsequence
                tails.append(num)
            else:
                # Replace tails[x] with num
                # This gives us a better (smaller) tail for subsequences of length x+1
                tails[x] = num
        
        # Length of tails = length of LIS
        return len(tails)

"""
    Last Looked
    11-12-25

"""