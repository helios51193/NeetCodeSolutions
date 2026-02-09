from heapq import heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.is_val_in_heap = set()
        self.min_val = 1

    def popSmallest(self) -> int:
        if not self.heap:
            smallest = self.min_val
            self.min_val += 1
        else:
            smallest = heappop(self.heap)
            self.is_val_in_heap.remove(smallest)
        return smallest
        
    def addBack(self, num: int) -> None:
        if num >= self.min_val or num in self.is_val_in_heap:
            return
        elif num == self.min_val - 1:
            self.min_val -= 1
        else:
            heappush(self.heap, num)
            self.is_val_in_heap.add(num)