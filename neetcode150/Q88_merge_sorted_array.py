# Solution 1 
# Copy all the values in the of num2 in num1 and then sort
from typing import List


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,m+n):
            nums1[i] = nums2[i-m]
        
        nums1.sort()

# Solution 2
# Merge the two array in a third array (like it is done in merge sort) and then copy the temp array to the nums1 
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n < 1:
            return
        
        nums3 = [0 for x in range(m+n)]
        i = 0
        j = 0
        k = 0
        while i < m  and j < n:
            
            if nums1[i] < nums2[j]:
                nums3[k] = nums1[i]
                i += 1
            else:
                nums3[k] = nums2[j]
                j += 1
            
            k +=1
            
        while j < n:
            nums3[k] = nums2[j]
            k += 1
            j += 1
        
        while i < m:
            nums3[k] = nums1[i]
            k += 1
            i += 1
        
        for index, num in enumerate(nums3):
            nums1[index] = num
"""
    Last Looked
    1-11-25

"""
        