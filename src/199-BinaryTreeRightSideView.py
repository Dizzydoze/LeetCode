# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """level traverse, rightmost node on each level added"""
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = list()
        while stack:
            # traverse to the end of current level
            for _ in range(len(stack)):
                cur = stack.pop(0)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            # the rightmost node is the one we see
            res.append(cur.val)
        return res
