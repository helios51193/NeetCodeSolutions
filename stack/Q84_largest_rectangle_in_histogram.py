class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0 # for saving max height
        stack = [] # monotinic stac
        
        # loop over all the heights
        for i, height in enumerate(heights):
            start_idx = i
            # pop till current height is less that the stack top height
            # and calculate max area for each bar
            while stack and  height < stack[-1][1]:
                top_idx, top_height = stack.pop()
                max_area = max(max_area, top_height * (i-top_idx))
                start_idx = top_idx
            
            # append the updated start index and the height
            stack.append((start_idx, height))
        
        print(stack)
        print(max_area)

        # Calculate the area of histogram
        for i, height in stack:
            max_width = len(heights)-i
            max_area = max(max_area, height * max_width)
        
        return max_area
        
