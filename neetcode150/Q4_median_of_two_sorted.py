# Brute force
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        num3 = nums1 + nums2
        num3.sort()
        if len(num3) %2 == 0:
            
            a = len(num3)//2
            b = len(num3)//2 - 1
            return (num3[a] + num3[b])/2
        return num3[len(num3)//2]

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minX = float('inf') if partitionX == m else nums1[partitionX]
            minY = float('inf') if partitionY == n else nums2[partitionY]
            
            if maxX <= minY and maxY <= minX:
                if (m + n) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1


"""
    Last Looked
    04-12-25

"""  