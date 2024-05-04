class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # convert list to a set
        nums_set = set(nums)
        mx = 0
        for num in nums:
            # check if num-1 is in the set
            # if num-1 is not in the set, it means that it is the first in the sequence
            if num-1 not in nums_set:
                tmp = 1
                # loop till num+1 is in the set
                while num+tmp in nums_set:
                    tmp +=1
                # take the max between the previous and current consecutive count
                mx = max(mx,tmp)
        
        return mx