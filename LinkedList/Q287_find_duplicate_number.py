# using set (can also use dict)
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        mp = set()
        #mp = {}
        for ele in nums:
            if ele in mp:
                return ele
            else:
                mp.add(ele)
                #mp[ele] = 1

# using index
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            n = abs(nums[i]) - 1
            if nums[n] < 0:
                return n+1
            nums[n] *=-1


        