# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equal(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            return root.val == subRoot.val and self.equal(root.left, subRoot.left) and \
                self.equal(root.right, subRoot.right)
        return root is None and subRoot is None

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.equal(root, subRoot):
            return True
        elif root and subRoot:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return (subRoot is None) or (root is not None)