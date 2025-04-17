from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        triplets = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i]== nums[i-1]:
                continue # skip already checked the first number
            firstNum = nums[i]
            j = i+1
            k = len(nums) - 1
            while j < k:
                secondNum = nums[j] #Iterate using 2 pointers to get the desired sum
                thirdNum = nums[k]
                potentialSum = firstNum + secondNum + thirdNum
                if potentialSum > 0:
                    k -=1 #Move left to smaller value
                elif potentialSum < 0:
                    j += 1 # Move righ to bigger value
                else:
                    triplets.add((firstNum, secondNum, thirdNum))
                    j += 1
                    k -= 1
                
                    while j < k and nums[j] == nums[j-1]: 
                        j+= 1 #skip if next are duplicates
                    
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1  #skip if next are duplicates
    
        return list(triplets)