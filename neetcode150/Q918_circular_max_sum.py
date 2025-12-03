#https://leetcode.com/problems/maximum-sum-circular-subarray/description/?envType=study-plan-v2&envId=top-interview-150

"""

Two cases

case 1
| --- MAX SUM --- | ** MIN SUM ** | 

case 2 (Circular)
| * MIN * | -- MAX SUM -- | * SUM * |

"""

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        total_sum = nums[0]
        for i in range(1, len(nums)):

            curr_max = max(curr_max + nums[i], nums[i])
            max_sum = max(max_sum, curr_max)

            curr_min = min(curr_min + nums[i], nums[i])
            min_sum = min(min_sum, curr_min)

            total_sum += nums[i]

        circular_sum = total_sum - min_sum

        # The max/min sum is not circular
        if circular_sum == 0:
            return max_sum
        
        return max(max_sum, circular_sum)

# More simlified and consice
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def min_sum():
            min_res = nums[0]
            cur = 0
            for r in nums[1:]:
                if cur > 0 and r < 0:
                    cur = r
                else:
                    cur += r
                min_res = min(min_res, cur)

            return min_res

        def max_sum():
            max_res = -float("inf")
            cur = 0
            for r in nums:
                if cur < 0:
                    cur = r
                else:
                    cur += r
                max_res = max(max_res, cur)
            return max_res

        # return max_sum()
        return max(max_sum(), sum(nums) - min_sum())


"""
    Last Looked
    03-12-25

"""