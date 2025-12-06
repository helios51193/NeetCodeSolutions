import heapq

# using heap, mantain k count heap for optimization
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        # heap = nums[:k]
        # heapq.heapify(heap)
        # for k in nums[k:]:
        #     if k > heap[0]:
        #         heapq.heapreplace(heap,k)
        # return heap[0]

        return heapq.nlargest(k, nums)[-1]




"""
    Last Looked
    06-12-25

"""  