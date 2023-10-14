# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """[DFS] Depth-First Search"""
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def construct_path(root, path):
            if root:
                path += str(root.val)
                # we reach the leaf node
                if not root.left and not root.right:
                    # save current path as result
                    paths.append(path)
                    # reset path for new start
                    path = ''
                # there's still way to go deeper
                else:
                    path += '->'
                    construct_path(root.left, path)
                    construct_path(root.right, path)

        path = ''
        paths = list()
        construct_path(root, path)
        return paths
