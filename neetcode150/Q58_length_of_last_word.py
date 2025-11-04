class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.rstrip()
        words = s.split(" ")
        return len(words[-1])

"""
    Last Looked
    1-11-25

"""