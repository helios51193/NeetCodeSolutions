class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers)-1
        while(left < right):
            numsum = numbers[left] + numbers[right]
            if numsum == target:
                return [left+1, right+1]
            if numsum > target:
                right -=1
            else:
                left += 1
        
        return []

