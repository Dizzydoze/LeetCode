# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):
        def get_height(root):
            curr = root
            h = 0
            while curr:
                h += 1
                # always go left, ensure the height of right child
                curr = curr.left
            return h

        # num nodes of complete binary tree = 2^h + 1
        if not root:
            return 0
        left_height = get_height(root.left)
        right_height = get_height(root.right)

        # root.left is complete binary tree, num node = 2^h + 1
        # root.right counted by recursion
        # remember root node + 1
        if left_height == right_height:
            return (2 ** left_height - 1) + self.countNodes(root.right) + 1
        # root.right is complete binary tree, num node = 2^h + 1
        # root.left counted by recursion
        # remember root node + 1
        else:
            return (2 ** right_height - 1) + self.countNodes(root.left) + 1
