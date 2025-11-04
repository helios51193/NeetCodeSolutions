from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
       
        # Check if only one element in array
        if len(citations) == 1 and citations[0] > 1: 
            return 1

        sorted_citation = sorted(citations, reverse=True)


        # If all the citations are > than size of size , return the size 
        if sorted_citation[-1] >= len(sorted_citation):
            return len(sorted_citation)
        
        # Check if the ith paper has fewer than i+1 citations
        for i in range(len(sorted_citation)):
            if sorted_citation[i] < i+1:
                return i
        
        return 0

"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)

        # Count how many papers have i citations
        for c in citations:
            if c >= n:
                count[n] += 1  # Cap at n
            else:
                count[c] += 1

        total = 0
        # Traverse from high to low
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i

        return 0

"""
"""
    Last Looked
    1-11-25

"""  