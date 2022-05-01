class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        # bottom up DP
        bottom_up = [0] * n
        bottom_up[0] = 1
        bottom_up[1] = 2
        for i in range(2, n):
            bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
        return bottom_up[n - 1]
