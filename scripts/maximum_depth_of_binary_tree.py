class Solution:
    def maxDepth(self, root) -> int:
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            # Calculate from the bottom
            return max(left + 1, right + 1)

        return dfs(root)
