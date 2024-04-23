
# As every anagram will have the same characters, their order when sorted will be same.
# We can use this property to group the string. The strings who yields same string when ordered by alphabet will belong to same group  
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anag_grps = {}
        for anag in strs:
            key = ".".join(sorted(anag))
            if key in anag_grps:
                anag_grps[key].append(anag)
            else:
                anag_grps[key] = [anag]

        return anag_grps.values()  

# Solution - 2
# Same solution but with default dict. Helps remove the condition
from collections import defaultdict 
# Solution - 1
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anag_grps = defaultdict(list)
        for anag in strs:
            key = ".".join(sorted(anag))
            anag_grps[key].append(anag)

        return anag_grps.values()   