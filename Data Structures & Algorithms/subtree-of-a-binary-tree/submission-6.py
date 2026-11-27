# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        elif root is None:
            return False
        if self.same(root, subRoot): # equal, not just val.
            return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def same(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        return p.val == q.val and self.same(p.left, q.left) and self.same(p.right, q.right)