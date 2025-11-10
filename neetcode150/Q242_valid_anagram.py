# using hashmap
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        char_map = {}
        for char in s:
            char_map[char] = char_map.get(char,0) + 1
        
        for char in t:
            if char not in char_map:
                return False
            
            char_map[char] -= 1
            if char_map[char] < 0:
                return False
        
        return True


# using Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

"""
    Last Looked
    10-11-25

"""