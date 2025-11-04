# Solution 1
from typing import List


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        # create a hashmap to count the occurences of nums 
        m_dict = {}
        for num in nums:
            if num not in m_dict:
                m_dict[num] = 1
            else:
                m_dict[num] +=1
        
        # find the key for which count  > n/2
        for k,v in m_dict.items():
            if v > len(nums)/2:
                return k

# Solution 2
# with better optimizations
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # create a hashmap to count the occurences of nums 
        m_dict = {}
        req = len(nums)/2
        for num in nums:
            m_dict[num] = m_dict.get(num,0) +1

            if m_dict[num] > req:
                return num

## Note :- Boyer Moors Voting Algorithm
"""
    Last Looked
    1-11-25

"""