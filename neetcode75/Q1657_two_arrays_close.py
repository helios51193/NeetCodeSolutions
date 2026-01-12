from typing import Counter

# O(nlogn) solution, can be done in O(n) by using dict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        f1,f2 = Counter(word1), Counter(word2)

        if set(f1.keys()) != set(f2.keys()):
            return False
        
        return sorted(f1.values()) == sorted(f2.values())

"""
    Last Looked
    12-01-26

"""  