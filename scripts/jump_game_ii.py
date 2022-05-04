class Solution:
    def jump(self, nums) -> int:
        # edge case: [0]
        if len(nums) == 1:
            return 0
        max_jump, minimal_steps, jump_point = 0, 0, 0
        for i, v in enumerate(nums):
            max_jump = max(max_jump, i + v)
            if max_jump >= len(nums) - 1:
                minimal_steps += 1
                break
            if i == jump_point:
                minimal_steps += 1
                jump_point = max_jump
        return minimal_steps
