# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionStack:
    """stack pre-order traverse"""
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # add all nodes including None into the stack during iteration
        stack = [(p, q)]
        while stack:
            curp, curq = stack.pop()
            # both None, no more children, just keep popping
            if not curp and not curq:
                continue
            # different structure
            if not curp or not curq:
                return False
            # same structure, different value
            if curp.val != curq.val:
                return False
            # else they are both not None and got the same value
            stack.append((curp.right, curq.right))
            stack.append((curp.left, curq.left))
        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionRecursion:
    """recursion"""
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # termination condition
        # both nodes are None, they reach the end without return False, meaning they are the same
        if not p and not q:
            return True
        # different structure
        if not p or not q:
            return False
        # same structure but different values
        if p.val != q.val:
            return False
        # else they are not None with same values, going deeper on both sides
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
