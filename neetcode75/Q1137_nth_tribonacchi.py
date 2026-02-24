class Solution:
    def tribonacci(self, n: int) -> int:
        
        t0, t1, t2 = 0,1,1
        if n ==0:
            return t0
        if n == 1:
            return t1
        if n == 2:
            return t2
        res = 0
        for _ in range(2, n):
            res = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = res
        return res


"""
    Last Looked
    23-02-26

"""  