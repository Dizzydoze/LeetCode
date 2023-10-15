# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """deque for iteration. range length for each level"""
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        # deque iteration
        q = [root]
        res = list()
        while q:
            # get all node value from only [current level] and save them
            level_len, level = len(q), list()
            for i in range(level_len):
                cur = q.pop(0)  # pop left
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)
        return res[::-1]
