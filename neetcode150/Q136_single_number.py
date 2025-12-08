class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        res = nums[0]
        for x in nums[1:]:
            res ^= x
        
        return res


"""
    property of xor = if xor self number converts to 0 , xoring 0 with any number gives the number
"""

"""
    Last Looked
    07-12-25

"""    