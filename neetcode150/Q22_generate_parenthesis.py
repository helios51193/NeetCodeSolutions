class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        def backtrack(S="", left=0, right=0):
            if len(S) == 2 * n:
                result.append(S)
                return
            
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)


        result = []
        backtrack()
        return result


"""
    The solution is based on essentially 4 points
    1. If we have option to add left '(', then we add, and mark the string as unbalanced
    2. If we have option to add right ')' by checking unbalanced , then add it and mark the string as balanced.
    3. The checking of balanced/unbalanced can be made in different ways - tallying left and right count, count for balanced,
    4. Check whether to add left before checking balance. 


"""

"""
    Last Looked
    30-11-25

"""
"""
Alternate Solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, t):
            if l > n or r > n or l < r:
                return
            if l == n and r == n:
                ans.append(t)
                return
            dfs(l + 1, r, t + '(')
            dfs(l, r + 1, t + ')')

        ans = []
        dfs(0, 0, '')
        return ans
"""