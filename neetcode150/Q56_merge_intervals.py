from operator import itemgetter
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []
        
        intervals.sort(key=itemgetter(0))
        
        merged_intervals = []

        current_start, current_end = intervals[0]
        for start, end in intervals[1:]:
            if start <=current_end:
                current_end = max(current_end, end)
            else:
                merged_intervals.append([current_start, current_end])
                current_start, current_end = start, end

        merged_intervals.append([current_start, current_end])
        return merged_intervals
