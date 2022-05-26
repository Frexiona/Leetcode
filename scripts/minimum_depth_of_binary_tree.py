class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        # If there's no conditions:
        # if not root.left: and if not root.right:
        # Then for tree node only has one child (e.g. left), it will only
        # calculate min(left, right), which right = 0
        # so the result will always be 0 in this case even though it's not leaf node
        return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)
