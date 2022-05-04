class Solution:
    def canJump(self, nums):
        # # enumeration: too slow, O(n^2)
        # total_steps = len(nums) - 1
        # if total_steps == 0:
        #     return True
        # found = False
        # for add in range(1, nums[0] + 1):
        #     if add >= total_steps + 1:
        #         break
        #     if self.canJump(nums[add:]):
        #         return True
        # return False

        # find the max jump
        max_jump = 0
        for i, v in enumerate(nums):
            if i > max_jump:
                return False
            if (i + v) >= (len(nums) - 1):
                return True
            max_jump = max(max_jump, i + v)
        return True
