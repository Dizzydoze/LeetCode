# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        # POSTORDER LEFT -> RIGHT -> CUR
        stack1 = [root]
        stack2 = []
        while stack1:
            cur = stack1.pop()
            stack2.append(cur)
            # Stack1: CUR -->
            # Stack2: CUR <--
            # Stack1: CUR.RIGHT <-- CUR.LEFT <--
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)
        # Stack2: CUR <-- CUR.RIGHT <-- CUR.LEFT, POSTORDER.
        return [stack2[i].val for i in range(len(stack2)-1, -1, -1)]
