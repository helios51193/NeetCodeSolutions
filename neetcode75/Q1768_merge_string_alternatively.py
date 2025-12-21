class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        m,n, toggle = len(word1), len(word2), True
        result = []
        i,j = 0,0
        while i < m and j < n:
            if toggle:
                result.append(word1[i])
                i+=1
            else:
                result.append(word2[j])
                j+=1
            
            toggle = not toggle
        
        if i == m:
            result.extend(word2[j:])
        elif j == n:
            result.extend(word1[i:])
        
        return "".join(result) 


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        wl1 = [*word1]
        wl2 = [*word2]
        cwl1 = len(wl1)
        cwl2 = len(wl2)
  
        
        least = min(cwl1,cwl2)
        merged = []
        
        for i in range(least):
            merged.append(wl1[i])
            merged.append(wl2[i])

        if cwl1 > cwl2:
            merged = merged + wl1[i+1:]
        elif cwl2 > cwl1:
            merged = merged + wl2[i+1:]




        return "".join(merged)


"""
    Last Looked
    21-12-25

"""  