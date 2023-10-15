# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """# level traverse, deque, z == -1 flag"""
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        res = list()
        z = -1
        while queue:
            level = list()
            for _ in range(len(queue)):
                if z == 1:  # popright, append left
                    cur = queue.pop()
                    level.append(cur.val)
                    # left later --> right first--> queue
                    if cur.right:
                        queue.appendleft(cur.right)
                    if cur.left:
                        queue.appendleft(cur.left)
                else:  # popleft, append right
                    cur = queue.popleft()
                    level.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            res.append(level)
            z *= -1
        return res
