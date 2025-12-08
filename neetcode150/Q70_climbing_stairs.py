
# works like a fibonacchi series, n upto 3 steps, 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=3:
            return  n
        
        prev1 = 3
        prev2 = 2
        cur = 0

        for _ in range(3, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        
        return cur

"""
    Last Looked
    08-12-25

"""