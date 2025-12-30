# we have to handle non-zeros , not zeros
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        anchor = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[anchor] = nums[anchor], nums[i]
                anchor += 1 

"""
    Last Looked
    30-12-25

""" 