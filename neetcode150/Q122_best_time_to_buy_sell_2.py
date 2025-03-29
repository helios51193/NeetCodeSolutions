from typing import List

# Solution 1
# We should buy only when there is a rise. Accumulate all the profit that can happen when 
# the price rises and we will get the correct answer 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        profit = 0
        for i in range(1,n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit