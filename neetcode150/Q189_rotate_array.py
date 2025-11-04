# Solution 1 -using insert and pop
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0,nums.pop())

# Solution 2 - using array splicing
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
"""

"""
    Last Looked
    1-11-25

"""