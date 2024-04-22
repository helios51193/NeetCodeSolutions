# Solution 1 using set
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        len1 = len(nums)
        len2 = len(set(nums))

        return len1 != len2

# Solution 2 using dict
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        dups = {}
        for n in nums:
            if n not in dups:
                dups[n] = 1
            else:
                return True
        
        return False