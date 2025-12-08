class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        return x**n

# log n solution
# check the power formula 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def fnc(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent %2 == 0:
                return fnc(base * base, exponent//2)
            else:
                return base * fnc(base * base, (exponent - 1)//2)

        f = fnc()
        return float(f) if n >= 0 else 1/f

"""
    Last Looked
    08-12-25

"""