class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


"""
    why binary search on an unsorted array is working ?
    reason. Assumption is atlease 1 peak element. we


    Most people have figured out the binary search solution but are not able to understand how its working. 
    I will try to explain it simply. What we are essentially doing is going in the direction of the rising slope(by choosing the element which is greater than current). 
    How does that guarantee the result? Think about it, 
    there are 2 possibilities.a) rising slope has to keep rising till end of the array b) rising slope will encounter a lesser element and go down.
"""
"""
    Last Looked
    04-12-25

"""