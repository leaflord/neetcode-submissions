# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def bst(root: Optional[TreeNode], minval = -1000000000, maxval = 1000000000) -> bool:
    out = root is not None
    if root.left:
        out = out and minval < root.left.val < root.val
        out = out and bst(root.left, minval, root.val)
    if root.right:
        out = out and maxval > root.right.val > root.val
        out = out and bst(root.right, root.val, maxval)
    return out

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return bst(root)