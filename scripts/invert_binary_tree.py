class Solution:
    def invertTree(self, root):
        '''
        if root exists: flip,
        then return root as root has been changes
        '''
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(
                root.left
            )
        return root
