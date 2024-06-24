#Solution- Basic solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = nums1 + nums2
        arr = sorted(arr)
        if len(arr)%2 != 0:
            ind= len(arr)//2
            return arr[ind]
        else:
            ind=int(len(arr)/2)
            return (arr[ind]+arr[ind-1])/2


#Solution- using binary search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1
        part = (n1 + n2 + 1)//2
        n = n1 + n2

        while low <=  high:
            mid1 = (low + high)//2
            mid2 = part- mid1
            l1 = nums1[mid1 - 1] if mid1 > 0 else -float('inf')
            l2 = nums2[mid2 - 1] if mid2 > 0 else -float('inf')
            r1 = nums1[mid1] if mid1 < n1 else float('inf')
            r2 = nums2[mid2] if mid2 < n2 else float('inf')

            if l1 <=r2 and l2 <=r1:
                if n%2 == 1:
                    return max(l1,l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 >  r2:
                high = mid1 -1
            else:
                low = mid1 + 1
        return -1
        
