class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        
        def backtrack(first = 1, curr = []):

            if len(curr) == k:
                output.append(curr[:])
                return
            
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
            
        output = []
        backtrack()
        return output

"""
    Last Looked
    28-11-25

""" 