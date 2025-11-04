from typing import List

# Solution 1
# index point to the next space we have to put element on
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 2
        for i in range(2, len(nums)):
            # check if the element encountered is the third copy, if yes continue
            if nums[i] == nums[index-1] and nums[i] == nums[index-2]:
                continue
            else:
                # copy it to the current index and increment the index
                nums[index] = nums[i]
                index+=1
        
        return index


# Solution 2
# using a dict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        # add number as key and value is the count 
        # if count is >2 , clamp it to 2
        count_map = {}
        for i in nums:
            count_map[i] = min(count_map.get(i,0) + 1,2)

        # Iterate over the dict and create a list and copy it to the original
        temp = []
        for i,c in count_map.items():
            temp.extend([i for _ in range(c)])
        
        for i,x in enumerate(temp):
            nums[i] = x
        
        return len(temp)

"""
    Last Looked
    1-11-25

"""