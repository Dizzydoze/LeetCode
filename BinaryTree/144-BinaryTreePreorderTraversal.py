# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        # Preorder CUR -> LEFT -> RIGHT
        cur = root
        stack = []  # stack stores nodes waiting to check right
        res = []    # stores proceed nodes
        while cur or stack:     # keep proceed until stack is empty
            while cur:
                res.append(cur.val)     # proceed cur node, store value
                stack.append(cur)       # push into stack after proceeding
                cur = cur.left          # keep going left until None
            # Left is None, pop out previous node and start to go Right
            cur = stack.pop()   # keep poping if Right is None
            cur = cur.right
        return res