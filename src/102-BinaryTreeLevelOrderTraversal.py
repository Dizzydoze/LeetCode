# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level traverse
        if not root:
            return []
        queue = [root]
        res = list()
        while queue:
            level = list()
            for _ in range(len(queue)):     # traverse current level
                cur = queue.pop(0)  # pop left
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)  # append right
                if cur.right:
                    queue.append(cur.right) # append right
            res.append(level)
        return res
