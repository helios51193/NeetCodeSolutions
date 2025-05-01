from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []

        for interval in intervals:
            # new interval starting is outside the current interval, 
            if interval[1] < newInterval[0]:
                result.append(interval)
            
            # the new interval's range is before the current interval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            
            # new interval is overalling the current inerval
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            
        
        result.append(newInterval)
        return result