# using dictionary
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

# using Linked List (slower in python)
class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = None,None
        self.map = {}
        

    def get(self, key: int) -> int:
       
        if key not in self.map:
            return -1
        curr_node = self.map[key][1]
        
        if curr_node != self.tail:
            if curr_node == self.head:
                self.head = self.head.next
            else:
                prev_node = curr_node.prev
                next_node = curr_node.next
                prev_node.next = next_node 
                if next_node:
                    next_node.prev = prev_node 
            
            curr_node.prev = self.tail
            self.tail.next = curr_node
            self.tail = curr_node
            curr_node.next = None

        return self.map[key][0]
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.map:
            self.map[key][0] = value
            self.get(key)
            return
        
        if len(self.map) == self.capacity:
            del self.map[self.head.val]
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
        
        new_entry = Node(key, self.tail, None)
        if not self.head:
            self.head = new_entry
        else:
            self.tail.next = new_entry
        self.tail = new_entry

        self.map[key] = [value, new_entry]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)