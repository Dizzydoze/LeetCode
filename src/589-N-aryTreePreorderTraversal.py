"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # stack
        stack = [root]
        res = []
        if not root:
            return
        while stack:
            curr = stack.pop()
            # preorder, handle root node first
            res.append(curr.val)
            for i in range(len(curr.children)-1, -1, -1):
                stack.append(curr.children[i])
        return res
