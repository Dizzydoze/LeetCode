# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # DFS with recursion
        if not root or root == p or root == q:
            return root
        # Keep search down until we reach None or find p and q
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        # both l and r are found in different subtrees of [current root]
        # recursion will keep going back "level up" until both l and r are found
        if l and r:
            return root
        # left found, return left; right found, return right; None found, return None
        return l or r
