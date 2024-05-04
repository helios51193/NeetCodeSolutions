class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 2
        for i in range(2, len(nums)):
            if nums[i] == nums[index-1] and nums[i] == nums[index-2]:
                continue
            else:
                nums[index] = nums[i]
                index+=1
        
        return index