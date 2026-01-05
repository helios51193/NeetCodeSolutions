# using sorting
from typing import Counter


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        count = 0

        while i < j:
            total = nums[i] + nums[j]
            if total == k:
                count += 1
                i += 1
                j -= 1
            elif total > k:
                j -= 1
            else:
                i += 1

# using hashmap
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        freq = Counter(nums)
        count = 0

        for x in nums:
            if freq[x] > 0 and freq[k - x] > 0:
                if x == k - x and freq[x] < 2:
                    continue
                freq[x] -= 1
                freq[k - x] -= 1
                count += 1

        return count
