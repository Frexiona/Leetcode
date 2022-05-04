class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                # dp[i] < dp[j] + 1: only +1 when j has larger or equal size of subsequence
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
