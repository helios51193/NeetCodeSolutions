from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        low, high = ceil(sum(piles)/h), max(piles)
        speed  = 0
        while low <=high:
            curr_speed = 0
            mid = (low + high)//2
            curr_speed = sum([ceil(piles[x]/mid) for x in range(len(piles))]) 
            if curr_speed <= h:
                speed = mid
                high = mid-1
            else:
                low=mid+1
        
        return speed
        