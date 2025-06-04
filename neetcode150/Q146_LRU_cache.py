class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_hash = {-1:-1}
        

    def get(self, key: int) -> int:
        if key not in self.lru_hash:
            return -1
        self.lru_hash[key] = self.lru_hash.pop(key)
        return self.lru_hash[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru_hash:
            self.lru_hash.pop(key)
        self.lru_hash[key] = value
        if len(self.lru_hash) > self.capacity:
            self.lru_hash.pop(next(iter(self.lru_hash)))
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)