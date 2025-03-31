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


        