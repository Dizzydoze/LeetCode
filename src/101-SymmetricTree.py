# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """Iteration with stack"""
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # adding two nodes into stack each time
        left, right = [root], [root]
        while left or right:
            l, r = left.pop(), right.pop()
            # both reach None, continue
            if not l and not r:
                continue
            # different structure, one is None, one is Not
            elif not l or not r:
                return False
            # same structure, different value
            elif l.val != r.val:
                return False
            # KEY: Mirror: be careful of the order
            # left traverse: cur -> left -> right, add right into stack first
            # right traverse: cur -> right -> left, add left into stack first
            left.append(l.right)
            left.append(l.left)
            right.append(r.left)
            right.append(r.right)
        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    """Recursion"""
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(left, right):
            # reach the end of cur path, meaning previous check is passed
            if not left and not right:
                return True
            # different structure, one is None
            elif not left or not right:
                return False
            # same structure, different value
            elif left.val != right.val:
                return False
            # KEY: MIRROR: left.left <-> right.right; left.right <-> right.left
            return isSym(left.left, right.right) and isSym(left.right, right.left)
        # start from root.left and root.right
        return isSym(root.left, root.right)
