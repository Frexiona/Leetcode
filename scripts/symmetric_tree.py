class Solution:
    def isSymmetric(self, root) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, rootL, rootR) -> bool:
        if not rootL and not rootR:
            return True
        elif not rootL or not rootR:
            return False
        return (
            rootL.val == rootR.val
            and self.isMirror(rootL.left, rootR.right)
            and self.isMirror(rootL.right, rootR.left)
        )
