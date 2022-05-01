class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            # nums[i] is always the biggest value at it's possition added by previous elements
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        return max(nums)
