from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        
        # This is done to check whether both string follow the same pattern
        # Leet and Code will fail this 
        # but ABCABC and ABC will pass
        if str1 + str2 != str2 + str1:
            return ""

        # This will work after checking both string follow the same pattern
        return str1[:gcd(len(str1), len(str2))]


"""
    Last Looked
    21-12-25

"""  