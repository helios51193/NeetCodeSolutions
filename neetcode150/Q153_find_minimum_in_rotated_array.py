
# O(n) solution 
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(len(nums)):
                if nums[i] < nums[i-1]:
                    return nums[i]

# similar approach as Q162 -  find peak
# O (log n) solution
class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        
        return nums[left]

"""
    Last Looked
    04-12-25

"""    