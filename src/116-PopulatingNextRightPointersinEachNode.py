"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    """# level traverse"""
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = [root]
        while queue:
            level = list()
            for _ in range(len(queue)):
                cur = queue.pop(0)  # pop left
                level.append(cur)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            # all current level nodes stored in level list
            for i in range(1, len(level)):
                level[i - 1].next = level[i]
            # last node in level
            level[-1].next = None
        return root
