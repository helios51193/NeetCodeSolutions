class Solution:
    def maxArea(self, height: list[int]) -> int:

        
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            current_area = min(height[left],height[right]) * (right-left)
            max_area = max(max_area, current_area)
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        
        return max_area