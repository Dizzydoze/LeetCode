# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def constructMaximumBinaryTree(self, nums):
        # left, right, two pointers for boundary
        def construct(left, right):
            if left > right:
                return
            max_idx = left   # always pick left as max to compare
            for i in range(left+1, right+1):
                if nums[i] > nums[max_idx]:
                    max_idx = i  # update max_idx
            # construct nodes
            node = TreeNode(val=nums[max_idx])
            node.left = construct(left, max_idx - 1)  # dump the max_num
            node.right = construct(max_idx + 1, right)
            return node
        return construct(0, len(nums) - 1)
