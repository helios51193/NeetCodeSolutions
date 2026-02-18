from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []

        for spell in spells:
            left, right = 0, n-1

            index = -1

            while left <= right:
                mid = left + (right-left)//2
                if spell * potions[mid] >= success:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            ans.append(0 if index == -1 else n - index)
        
        return ans

"""
    Last Looked
    18-02-26

"""  