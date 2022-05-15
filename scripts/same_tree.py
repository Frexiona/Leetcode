class Solution:
    def isSameTree(self, p, q) -> bool:
        # All 3 cases:
        # p == q == None
        # p == None or q == None
        # p.val != q.val
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
