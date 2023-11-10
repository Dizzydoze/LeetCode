# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root) -> bool:
        buff = []
        # front iteration
        stack = [root]
        while stack:
            cur = stack.pop()  # left node pop first
            if cur:
                if len(buff) == 0:
                    buff.append(cur.val)
                elif cur.val not in buff:
                    return False
                stack.append(cur.right)
                stack.append(cur.left)
        return True
