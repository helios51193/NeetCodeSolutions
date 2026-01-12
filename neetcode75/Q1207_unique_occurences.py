from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = Counter(arr)
        return len(set(arr)) == len(set(counts.values()))

"""
    Last Looked
    12-01-26

"""  