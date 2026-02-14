# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess():
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:

        first, last  = 1, n
        while first <= last:
            mid = first + (last - first)//2
            x = guess(mid)
            if x == 0:
                return mid
            elif x == -1:
                last = mid -1
            else:
                first = mid + 1

        return -1

"""
    Last Looked
    14-02-26

"""  