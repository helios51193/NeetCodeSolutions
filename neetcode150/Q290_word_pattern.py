# same solution as isomorphic string but with character mapped to a string
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        
        sets={}
        sett={}

        s1 = pattern
        t1 = s.split(" ")

        if len(s1) != len(t1):
            return False

        for i in range(len(s1)):
            chars=s1[i]
            chart=t1[i]
            if chars not in sets and chart not in sett:
                sets[chars]=chart
                sett[chart]=chars
           
            elif chars in sets and sets[chars] != chart:  
                return False
            elif chart in sett and sett[chart] != chars: 
                return False
        return True


"""
    Last Looked
    10-11-25

"""