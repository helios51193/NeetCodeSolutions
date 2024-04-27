# Solution 1 -  using sorting
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        #create a counter dict
        counterDict = {x:nums.count(x) for x in set(nums)}
        
        #sort the items based on count in descending order
        topk = sorted(counterDict.items(), key=lambda x:x[1], reverse=True)[:k]
        return [x[0] for x in topk]
    
# Solution 2 - using a Heap
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        #create a counter dict
        counterDict = {x:nums.count(x) for x in set(nums)}
        
        #create a heap
        heap =  [(-y,x) for x,y in counterDict.items()]
        heapq.heapify(heap)

        topk = []
        for i in range(k):
            topk.append(heapq.heappop(heap)[1])
        
        return topk