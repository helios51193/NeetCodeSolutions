from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        n = len(nums)
        output = [0 for x in range(len(nums))]
        prefix_product = 1
        postfix_product = 1
        # calculate the prefix product
        for i in range(n):
            output[i] = prefix_product
            prefix_product *= nums[i]
        
        # calculate and multiply with postfix product
        for i in range(n-1,-1,-1):
            output[i] *= postfix_product
            postfix_product *= nums[i]
        
        return output