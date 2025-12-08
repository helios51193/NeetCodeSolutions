class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones, twos = 0, 0

        for num in nums:
            # Update ones and twos
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones  # The single number remains in "ones"

"""
ones contains that comes one time. remove which are in twos
two contains that comes two times. remove those which are in ones

This is a xor version of x mod 3 

"""

"""
    Last Looked
    07-12-25

"""    