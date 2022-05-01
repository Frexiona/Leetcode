class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for i in range(m)]
        for c in range(1, n):
            for r in range(1, m):
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        return grid[-1][-1]
