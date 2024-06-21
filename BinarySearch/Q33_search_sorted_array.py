class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 1
        right = n
        # First Find the pivot
        while left <= right:
            mid = left + (right-left)//2

            if mid == n or nums[mid] < nums[mid-1]:
                break
            
            if nums[0] > nums[mid]:
                right = mid-1
            else:
                left = mid + 1
        
        # Use the pivot for binary search the rotated array
        l,r = 0,n-1
        l += mid
        r += mid
        while l <=r:
            m = l + (r-l)//2
            print(m)
            if nums[m%n] == target:
                return m%n
            elif nums[m%n] < target:
                l = m+1
            else:
                r = m-1
        
        return -1
            


        