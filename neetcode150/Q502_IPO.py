import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        
        projects = sorted(zip(capital, profits))
        n = len(profits)
        heap = []
        i=0
        for _ in range(k):
            
            # put all the projects that can be undertaken, put -profit for max heap 
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1

            # Can't afford any projects
            if len(heap) == 0:
                break
            # It will return the max profit one
            w += -heapq.heappop(heap)
        
        return w

"""
    Last Looked
    06-12-25

"""  