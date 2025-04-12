class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # i =  will have the position of the starting in substring in the haystack
        # j,k = will be used to each item in the haystack and needle starting from i
        n = len(haystack)
        m = len(needle)
        for i in range(n):
            j = 0
            for k in range(i,n):
                if haystack[k] == needle[j]:
                    j+=1
                else:
                    break
                if j == m:
                    return i
        
        return -1