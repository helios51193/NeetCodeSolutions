# Solution 1 
# index shows where the last valid number. Invalid values are all in the right side
from typing import List


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index +=1
        return index

# Solution 2 
# return the len of array with removed value
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = [x for x in nums if x != val]

        nums[:] = temp
        return len(nums)