class Solution:
    """DFS Depth-First Search"""
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, path = list(), list()

        # backtracking
        def backtrack(n, k, start_index):
            # path is filled, no more num to pick, add to result and return
            if len(path) == k:
                # add copy of the path, not original reference of it
                res.append(path[:])
                return
            # still need to pick more numbers for path
            for i in range(start_index, n + 1):
                # add current num into path, form a new combination
                path.append(i)
                backtrack(n, k, i + 1)
                # remove previous num
                path.pop()
        backtrack(n, k, 1)
        return res
