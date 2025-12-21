class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        # find the max number of candies the kid have
        max_candy = max(candies)

        # optimized version of  candy + extra_candies >= max_candy
        # we have to give all the extra to one person and check whether that becomes greater than the current max.
        gauge = max_candy - extraCandies
        return [ c >= gauge for c in candies ]
    

"""
    Last Looked
    21-12-25

"""  