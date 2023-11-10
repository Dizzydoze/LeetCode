# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def inorderTraversal(self, root):
        # Inorder LEFT -> CUR -> RIGHT
        stack = []
        res = []
        cur = root
        # keep going LEFT until None, push each one into stack
        while cur or stack:
            if not cur:             # we reach the end of LEFT
                cur = stack.pop()   # pop previous node
                res.append(cur.val) # proceed
                cur = cur.right     # go RIGHT
            else:
                stack.append(cur)   # add cur node to stack whenever it's valid
                cur = cur.left      # keep going LEFT until it's None
        return res