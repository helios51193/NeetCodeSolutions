from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""
        if len(s) <  len(t):
            return ""
        
        need = Counter(t)
        window = {}
        have = 0
        need_total = len(need)
        res = [-1, -1]
        res_len = float("inf")

        left  = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            
            # When we have all required chars, try to shrink from left
            while have == need_total:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Try to shrink the window, if shrunk then ok 
                # else will start search of a new substring.
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
    
        l,r = res
        return s[l:r+1] if res_len != float("inf") else ""


            

                

        
        