# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """recursion"""
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # termination conditions
        # it will return None if both are None
        if not root1:
            return root2
        if not root2:
            return root1
        # if both are not None, create a new node with sum value
        merged = TreeNode(val=root1.val + root2.val)
        # send left nodes to merge, reconnect it after return
        merged.left = self.mergeTrees(root1.left, root2.left)
        # send right nodes to merge, reconnect it after return
        merged.right = self.mergeTrees(root1.right, root2.right)
        # return current root
        return merged
