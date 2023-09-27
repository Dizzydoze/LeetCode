# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def maxDepth(self, root):
        # BFS
        if not root:
            return 0
        depth = 0
        # queue stores all nodes on current level
        queue = collections.deque()
        queue.append(root)
        while queue:
            # num of nodes on current level
            size = len(queue)
            while size > 0:
                curr = queue.pop()
                # order doesn't matter, just exhaust all nodes on current level
                if curr.left:
                    queue.appendleft(curr.left)
                if curr.right:
                    queue.appendleft(curr.right)
                size -= 1
            # previous level end, nodes on new level filled
            depth += 1
        return depth
