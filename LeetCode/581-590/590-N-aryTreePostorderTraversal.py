"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # postorder left > right > root
        if not root:
            return []
        # (double) stack, ans is actually reversed in the sec stack
        stack = [root]
        res = list()
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            for child in curr.children:
                stack.append(child)
        return res[::-1]
