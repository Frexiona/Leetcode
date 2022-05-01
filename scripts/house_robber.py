class Solution:
    def rob(self, nums):
        # problem -> sub-problem
        # # Too slow
        # if len(nums) == 1: return nums[0]
        # if len(nums) == 2: return max(nums)
        # return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        # example: [rob1, rob2, n, n + 1]
        rob1, rob2 = 0, 0
        for n in nums:
            n = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = n
        return rob2
