class Solution:
    def lowestCommonAncestor(self, root, p, q):
        '''
        Case_#1:
        Both p and q are smaller than current node, then search left-subtree by recursive
        Case_#2:
        Both p and q are larger than current node, then search right-subtree by recursive
        Case_#3:
        Both p and q are not on the same side of current node, then current node must be the Lowest common ancestor of ( p, q )
        '''
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
