
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 
        power = 31
        while n:
            # Extract the LSB from 1 and place it to the power th position
            # then shift the n to expose next bit in LSB and put it into (power - 1)th position and so on
            result += (n&1) << power
            n = n >> 1
            power -= 1 
        
        return result


"""
    Last Looked
    06-12-25

"""  