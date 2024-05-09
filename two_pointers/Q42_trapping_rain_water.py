class Solution:
    def trap(self, height: list[int]) -> int:
        left,right = 0, len(height)-1
        max_left = height[left]
        max_right = height[right]
        trapped_water = 0
        while left < right:
            if max_left < max_right:
                left +=1
                max_left = max(max_left, height[left])
                trapped_water += max_left - height[left]
            else:
                right -=1
                max_right = max(max_right, height[right])
                trapped_water += max_right - height[right]

        return trapped_water        