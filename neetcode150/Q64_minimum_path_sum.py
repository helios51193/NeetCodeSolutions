# O(n) space
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        m,n = len(grid), len(grid[0])

        dp = [0] * n
        dp[0] = grid[0][0]


        # for first row
        for j in range(1,n):
            dp[j] = dp[j-1] + grid[0][j]
        

        for i in range(1,m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        
        return dp[-1]

# O(1) space, destroys the input
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        #creating a prefix sum
        N_rows = len(grid)
        N_cols = len(grid[0])

        # First iterate for 1st row and 1st column
        for i in range(1,N_cols):
            grid[0][i] += grid[0][i-1]
        for i in range(1,N_rows):
            grid[i][0] += grid[i-1][0]
        
        # calculate for 1 to n and 1 to m
        for i in range(1,N_rows):
            for j in range(1,N_cols):
                grid[i][j] += grid[i-1][j] if grid[i-1][j] < grid[i][j-1] else grid[i][j-1]
        return grid[N_rows-1][N_cols-1]

"""
    Last Looked
    12-12-25

"""