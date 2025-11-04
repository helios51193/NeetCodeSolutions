import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        
        if cleaned == "" or cleaned == " ":
            return True
        
        return cleaned == cleaned[::-1]

"""
    Last Looked
    4-11-25

"""