# 2d DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = i
        
        for j in range(1, n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        
        return dp[m][n]

# 1DP+ recursion +  memoization
from functools import lru_cache

class Solution:
    def minDistance(self, word1, word2):
        @lru_cache(None)
        def dfs(i, j):
            if i == 0:
                return j
            if j == 0:
                return i

            if word1[i-1] == word2[j-1]:
                return dfs(i-1, j-1)

            return 1 + min(
                dfs(i-1, j),     # delete
                dfs(i, j-1),     # insert
                dfs(i-1, j-1)    # replace
            )

        return dfs(len(word1), len(word2))