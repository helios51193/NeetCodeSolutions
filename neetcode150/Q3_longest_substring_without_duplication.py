class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        seen = set()
        maxlen = 0

        for ch in s:
            while ch in seen:
                seen.remove(s[l])
                l +=1
            seen.add(ch)
            print(seen)
            if maxlen < len(seen):
                maxlen = len(seen)
        
        return maxlen
        