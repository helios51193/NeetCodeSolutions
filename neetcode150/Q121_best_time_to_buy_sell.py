class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        current_lowest = prices[0]
        max_profit = 0
        for i in prices[1:]:
            if current_lowest > i:
                current_lowest = i
            if max_profit < i-current_lowest:
                max_profit = i-current_lowest
        return max_profit