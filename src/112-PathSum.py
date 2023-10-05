# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """BFS Board First Search (deque)"""
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # pop left, append right
        # queue nodes stores node, cnts stores current path sum
        if not root:
            return False
        nodes = collections.deque([root])
        cnts = collections.deque([root.val])
        while nodes:
            cur = nodes.popleft()  # current node
            tmp = cnts.popleft()  # current path sum at this node
            if not cur.left and not cur.right and tmp == targetSum:  # leaf node reached
                return True
            if cur.left:
                nodes.append(cur.left)  # next node
                cnts.append(tmp + cur.left.val)  # next path sum at next node
            if cur.right:
                nodes.append(cur.right)
                cnts.append(tmp + cur.right.val)
        return False


class Solution2:
    """DFS Deep First Search (recursion)"""
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # termination condition
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)