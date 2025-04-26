from collections import defaultdict
from typing import List

# using sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 1 and strs[0] == "":
            return [[""]]
        anagrapm_map = defaultdict(list)

        for word in strs:
            sorted_str = "".join(sorted(word))
            anagrapm_map[sorted_str].append(word)
        
        return list(anagrapm_map.values())

# without using sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 1 and strs[0] == "":
            return [[""]]
        anagrapm_map = defaultdict(list)

        for word in strs:
            lst = [0] * 26
            for char in word:
                lst[ord(char) - ord('a')] += 1
            
            lst = tuple(lst)
            anagrapm_map[lst].append(word)

        return list(anagrapm_map.values())
        
