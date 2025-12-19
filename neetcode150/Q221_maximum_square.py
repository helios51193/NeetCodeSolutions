class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        
        m, n  = len(matrix), len(matrix[0])
        result = 0
        dp = [[0] * n for _ in range(m)]

        for i in  range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else: 
                    dp[i][j] = min(dp[i-1][j] + 1 ,
                                        dp[i][j-1] +  1 ,
                                        dp[i-1][j-1] +  1)
                    
                if dp[i][j] >  result:
                    result = dp[i][j]
        
        return result * result

"""
    Last Looked
    19 -11-25

"""