# using hashmap
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False
        sets={}
        sett={}
        for i in range(len(s)):
            chars=s[i]
            chart=t[i]
            if chars not in sets and chart not in sett:
                sets[chars]=chart
                sett[chart]=chars
           
            elif chars in sets and sets[chars] != chart:  
                return False
            elif chart in sett and sett[chart] != chars: 
                return False
        return True

# using python specific functions
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        zipped_set = set(zip(s,t))
        return len(zipped_set) == len(set(s)) == len(set(t))

"""
    Last Looked
    10-11-25

"""