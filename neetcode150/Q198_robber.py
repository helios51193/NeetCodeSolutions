class Solution:
    def rob(self, nums: list[int]) -> int:
        prev_rob = max_rob = 0

        for cur_val in nums:
            
                    # max(dp[i-1], dp[i-2] + num[i])
            temp = max(max_rob, prev_rob + cur_val)
            prev_rob = max_rob
            max_rob = temp
        
        return max_rob

"""
    Last Looked
    08-12-25

"""