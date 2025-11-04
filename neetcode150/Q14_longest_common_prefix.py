from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    
        if not strs:
            return ""
        
        prefix = strs[0]
        for x in strs[1:]:
            while not x.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
    
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        return self.divide_and_conquer(strs, 0, len(strs) - 1)

    def divide_and_conquer(self, strs, left, right):
        # Base case: one string
        if left == right:
            return strs[left]
        
        # Divide step
        mid = (left + right) // 2
        
        # Recurse for left and right halves
        lcp_left = self.divide_and_conquer(strs, left, mid)
        lcp_right = self.divide_and_conquer(strs, mid + 1, right)
        
        # Combine step: find common prefix of both halves
        return self.common_prefix(lcp_left, lcp_right)

    def common_prefix(self, left, right):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]
"""
"""
    Last Looked
    4-11-25

"""

