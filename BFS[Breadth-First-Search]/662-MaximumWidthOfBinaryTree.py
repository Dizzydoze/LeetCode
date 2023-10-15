# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """BFS[Breadth-First-Search]"""
    def widthOfBinaryTree(self, root):
        # mark node index, left * 2, right * 2 + 1
        # width will be right - left + 1
        width = 1
        queue = [[root, 1]]
        while queue:
            next_level = []  # for update the queue each level
            for node, index in queue:  # unpack
                # None won't be added and counted
                if node.left:
                    next_level.append([node.left, index*2])
                if node.right:
                    next_level.append([node.right, index*2+1])
            # count current level's width, tmp will be next level
            width = max(width, queue[-1][1] - queue[0][1] + 1)
            queue = next_level
        # next level is empty makes queue empty and break loop
        return width
