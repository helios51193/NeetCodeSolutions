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