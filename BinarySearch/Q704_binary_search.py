# Solution 1
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <=r:
            m = (l+r)//2 
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m+1
            else:
                r = m-1
        return -1

# Solution 2 - using recursion
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        def position(nums, target, f, l):
            if l >= f:
                m = (l+f)//2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    return position(nums, target, m+1, l)
                else:
                    return position(nums, target, f, m-1)
            else:
                return -1

        return (position(nums, target,0, len(nums)-1))