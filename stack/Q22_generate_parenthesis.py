class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def backtrack(S = [], left=0, right=0):
            # case when we left and right are n - base case
            # 2*n because count of number of all combinations is 2*n 
            if len(S) == 2 * n:
                pat = "".join(S)
                ans.append(pat)
                print(pat, left,right)
                return 
            # case when we can append left braces
            if left < n :
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            # case when we can append right braces when right braces is less than left braces
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()
        backtrack()
        print(ans)
        return ans