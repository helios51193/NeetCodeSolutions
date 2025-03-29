from typing import List
# Solution 1
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        current_lowest = prices[0]
        max_profit = 0
        # start the loop from second
        for i in prices[1:]:
            # select current if lower price is encountered
            if current_lowest > i:
                current_lowest = i
            # set the max profit if current calculated profit is better
            if max_profit < i-current_lowest:
                max_profit = i-current_lowest
        return max_profit

# Solution 2
# Same algo but with reversed list
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProf = 0
        currentMax = 0
        
        for i in reversed(prices):
            current_price = i
            if i > currentMax:
                currentMax = i
            if i < currentMax and (currentMax - i) > maxProf:
                maxProf = currentMax - i
        
        return maxProf