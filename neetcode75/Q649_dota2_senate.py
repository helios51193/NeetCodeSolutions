class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r = []
        d = []
        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            r_idx = r.pop(0)
            d_idx = d.pop(0)

            if r_idx < d_idx:
                r.append(r_idx + n)
            else:
                d.append(d_idx + n)
            
        return "Radiant" if r else "Dire"

"""
    Last Looked
    16-01-26
"""  