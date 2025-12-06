import heapq


class MedianFinder:

    def __init__(self):
        self.small_half = [] 
        self.large_half = []       


    # Invariants
    # all elements in small  < all elements in large
    # len(small) should be len(large) or len(large) +1
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_half, -1 * num) 
        heapq.heappush(self.large_half, -1 * heapq.heappop(self.small_half))

        if len(self.large_half) > len(self.small_half):
            heapq.heappush(self.small_half, -1 * heapq.heappop(self.large_half))

    def findMedian(self) -> float:
        if len(self.small_half) > len(self.large_half):
            return -1 * self.small_half[0]
        else:
            return (-1 * self.small_half[0] + self.large_half[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



"""
    Last Looked
    06-12-25

"""  