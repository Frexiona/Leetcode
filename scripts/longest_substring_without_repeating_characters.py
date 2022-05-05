class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        window = set()
        max_window = 0
        for right_pointer in range(len(s)):
            while s[right_pointer] in window:
                window.remove(s[left_pointer])
                left_pointer += 1
            window.add(s[right_pointer])
            max_window = max(max_window, right_pointer - left_pointer + 1)
        return max_window
