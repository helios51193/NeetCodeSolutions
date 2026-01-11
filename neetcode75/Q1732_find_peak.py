class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr = 0
        maxim = 0

        for i in gain:
            curr +=i
            maxim = max(curr, maxim)
        
        return maxim

"""
    Last Looked
    11-01-26

"""  