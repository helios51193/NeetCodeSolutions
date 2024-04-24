# Solution 1 
# create two arrays -  one with the product of elements to the left side of array and one with to the right side
# then multiply them
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        pre_product = [1] * len(nums)
        post_product = [1] * len(nums)

        # calculating pre-product
        for index in range(1, len(nums)):
            pre_product[index] = pre_product[index-1] * nums[index-1]
        
        # calculating post-product
        for index in range(len(nums)-2,-1,-1):
            post_product[index] = post_product[index+1] * nums[index+1]
        
        return [x*y for x,y in zip(post_product, pre_product)]

# Solution - 2 - with O(n) space if output array is considered
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        output = [1] * len(nums)
        # calculating pre-product
        for index in range(1, len(nums)):
            output[index] = output[index-1] * nums[index-1]
        
        fx = 1
        # calculating post-product
        for index in range(len(nums)-1,-1,-1):
            output[index] = fx * output[index]
            fx *= nums[index]
        
        return output