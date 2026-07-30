
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        ap = ancestors(root, p)
        aq = ancestors(root, q)
        lca = None
        for a, b in zip(ap, aq):
            if a is b:
                lca = a
            else:
                break
        return lca

def ancestors(root: TreeNode, t: TreeNode) -> List[TreeNode]:
    if not root:
        return list()
    if root.val == t.val:
        return [root]
    rest = ancestors(root.left, t)
    if not rest:
        rest = ancestors(root.right, t)
    if not rest:
        return list()
    return [root, *rest]
