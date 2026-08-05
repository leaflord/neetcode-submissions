class Solution:
    def isValidBST(self, root: Optional[TreeNode], minValue = -1001, maxValue = 1001) -> bool:
        if not root:
            return True
        if root.left and not (minValue < root.left.val < root.val):
            return False
        if root.right and not (root.val < root.right.val < maxValue):
            return False
        return self.isValidBST(root.left, minValue, root.val) and self.isValidBST(root.right, root.val, maxValue)