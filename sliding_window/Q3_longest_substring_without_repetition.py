# Solution 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        subs = []
        maxlen = 0
        for r in range(len(s)):
            # append till not in set
            if s[r] not in subs:
                subs.append(s[r])
            else:
                # remove the element,if exist, from the current substring 
                subs = subs[subs.index(s[r]) +1:]
                subs.append(s[r])
        
            if maxlen < len(subs):
                maxlen = len(subs)
        
        return maxlen

# Solution 2 -  using set 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        seen = set()
        maxlen = 0

        for ch in s:
            # remove till we are getting the same element
            while ch in seen:
                seen.remove(s[l])
                l +=1
            # after that add it to the seen, seen is the current substring
            seen.add(ch)
            if maxlen < len(seen):
                maxlen = len(seen)
        
        return maxlen
        