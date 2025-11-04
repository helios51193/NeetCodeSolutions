class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        # initialize list of string based on number of rows required
        # and fill them in a zig-zag fashion
        i = 0
        res = ["" for _ in range(numRows)] 

        for letter in list(s):
            if i == numRows-1:
                grow=False
            elif i == 0:
                grow=True
            res[i] += letter
            i = i+1 if grow else i-1    
        
        return "".join(res)



        # Example of iteration for PAYPALISHIRING with rows = 3

        #  P _ _
        #  P A _
        #  P A Y
        #  P AP Y 
        #  PA AP Y
        #  PA APL Y
        #  PA APL YI .... and so on
    
"""
Last Looked
4-11-25

"""