# Solution 1
# We iterate and try to find the index of the difference of the current num and the target num
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for index,nm in enumerate(nums):
            diff = target - nm
            if diff in nums and nums.index(diff) !=  index:
                return [index, nums.index(diff)]

# Solution 2
# used a hash-map to store the index for quick access.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        complement_map = {n:index for index,n in enumerate(nums)}
        print(complement_map)
        for index,nm in enumerate(nums):
           diff = target - nm
           print(diff)
           if diff in complement_map.keys() and complement_map[diff] != index:
                return [index,complement_map[diff]]