import random

# Use a list to store the actual values and a dict of value:index for O(1) search 
class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        self.arr.append(val)
        self.indices[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        i = self.indices[val]
        self.indices[self.arr[-1]] = i
        self.arr[i] = self.arr[-1]

        self.indices.pop(val)
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()