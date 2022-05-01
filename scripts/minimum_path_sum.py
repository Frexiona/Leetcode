class Solution:
    def minPathSum(self, grid):
        column_len = len(grid[0])
        row_len = len(grid)
        for c in range(1, column_len):
            grid[0][c] += grid[0][c - 1]
        for r in range(1, row_len):
            grid[r][0] += grid[r - 1][0]
        for c in range(1, column_len):
            for r in range(1, row_len):
                grid[r][c] += min(grid[r][c - 1], grid[r - 1][c])
        return grid[-1][-1]
