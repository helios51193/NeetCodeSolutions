
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a hashmap of the magazine and check if each letter of ransomnote is there in the map in right quantity
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_map = defaultdict(lambda: 0)
        for char in magazine:
            magazine_map[char] = magazine_map[char] + 1
        
        for char in ransomNote:

            if magazine_map.get(char,0) == 0:
                return False

            magazine_map[char] -=1
        
        return True
