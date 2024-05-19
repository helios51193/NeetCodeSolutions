#Solution 1 - using one pass
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

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

#Solution 2 - using left and right
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack= []
        lt = [None] * n
        rt = [None] * n
        for i in range(n):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0:
                lt[i] = -1
            else:
                lt[i] = stack[-1]
            stack.append(i)
        
        while len(stack) != 0:
            stack.pop()
        
        for i in range(n-1,-1,-1):
            
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0:
                rt[i] = n
            else:
                rt[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (rt[i] - lt[i] - 1))
        
        return max_area

        
        
