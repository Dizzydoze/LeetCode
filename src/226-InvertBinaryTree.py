# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recurtion base case
        if not root:
            return root
        # iterate through left tree
        self.invertTree(root.left)
        # iterate through right tree
        self.invertTree(root.right)
        # switch current root left and right child
        root.left, root.right = root.right, root.left
        return root





