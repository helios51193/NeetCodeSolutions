import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = list(zip(nums2, nums1))
        pairs.sort(reverse=True)

        heap = []
        curr_sum = 0
        max_score = 0

        for n2,n1 in pairs:
            heapq.heappush(heap, n1)
            curr_sum += n1
            if len(heap) > k:
                curr_sum-= heapq.heappop(heap)
            
            if len(heap) == k:
                max_score = max(max_score, curr_sum * n2)

        
        return max_score
    
    
"""
    Last Looked
    11-02-26

"""