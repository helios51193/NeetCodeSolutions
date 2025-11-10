# It is same as grouping the intervals , the difference 
# You sort it first, and group them till ending of current is greater then start of current point.
# One group can popped by 1 arrow.
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # sorting by end coordinates
        points.sort(key = lambda x:x[1])
        print(points)
        pop = points[0][1] # pop point
        arrow = 1 # number of arrows initialized
        for start,end in points:
            if pop < start:
                arrow += 1
                pop = end
        
        return arrow

"""
    Last Looked
    10-11-25

"""