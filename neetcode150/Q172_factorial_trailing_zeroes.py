class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count

"""
number of zeros is a combinations of contribution of 10 which is 2 *5. 2s will always be more than 5s. So it mostly depends on 5s only

number of zeroes = (n//5) + (n//25) + (n//125) ... toll n/5^k != 0
 

"""


"""
    Last Looked
    07-12-25

"""  