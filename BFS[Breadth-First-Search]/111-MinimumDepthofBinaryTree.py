# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """level traverse, return min depth once there's a leaf node in current level"""
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        queue = [root]
        mind = 1
        while queue:
            # traverse current level
            for _ in range(len(queue)):
                cur = queue.pop(0)  # pop left
                # cur is leaf node, return min depth
                if not cur.left and not cur.right:
                    return mind
                if cur.left:
                    queue.append(cur.left)   # append right
                if cur.right:
                    queue.append(cur.right)  # append right
            # move to next level, depth + 1
            mind += 1
        return mind
