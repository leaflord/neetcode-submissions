# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dig(root, level, cache):
    if not root:
        return
    # print(f"node:{root.val} level:{level} cache:{cache}\n")
    if level <= len(cache):
        cache[level - 1].append(root.val)
    else:
        cache.append([root.val])
    dig(root.left, level + 1, cache)
    dig(root.right, level + 1, cache)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        dig(root, 1, out)
        return out


