from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            # calculate the area and compare with the max area
            current_area = min(height[left],height[right]) * (right-left)
            max_area = max(max_area, current_area)
            # Move the shorter line, as moving the longer line does not capture more water.
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        
        return max_area