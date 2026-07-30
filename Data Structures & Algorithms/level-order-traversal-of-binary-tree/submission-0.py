class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def populate(node: Optional[TreeNode], level: int, out: List[List[int]]):
            if not node:
                return out
            if len(out) == level:
                out.append([])
            out[level].append(node.val)
            if node.left or node.right:
                populate(node.left, 1+level, out)
                populate(node.right, 1+level, out)
            return out
        out = []
        populate(root, 0, out)
        return out