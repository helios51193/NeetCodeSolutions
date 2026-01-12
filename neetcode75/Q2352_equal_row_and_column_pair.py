class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        
        n = len(grid)
        count = 0
        rows = {}

        # Hashing all the row
        for r in range(n):
            row = tuple(grid[r])
            rows[row] = 1 + rows.get(row,0)
        
        # fetch column and check if it exists in hashmap
        for c in range(n):
            col = tuple(grid[i][c] for i in range(n))
            count += rows.get(col, 0)
        
        return count


"""
    Last Looked
    12-01-26

"""  