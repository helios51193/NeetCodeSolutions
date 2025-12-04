
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        if nums == []:
            return [-1,-1]
        
        #searching for number in list
        start = 0
        l = len(nums)
        end = l-1
        num_index = -1
        while start <= end:
            mid = (start + end)//2
            print("mid",mid)
            if nums[mid] == target:
                num_index = mid
                break
            elif target < nums[mid]:
                end = mid-1
            else:
                start = mid + 1

        # find the middle and go left and right till you are getting the target.
        if num_index == -1:
            return [-1,-1]
        
        start = num_index
        print(num_index)
        while start >= 0 and nums[start] == target:
            start -=1

        end = num_index
        while end < l and nums[end] == target:
            end +=1
        
        return [start+1,end-1] 

"""
    Last Looked
    04-12-25

"""     