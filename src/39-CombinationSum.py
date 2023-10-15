class Solution:
    """DFS, Backtracking"""
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # use target == 0 with minus is better than sum()
        def dfs(candidates, begin, size, path, target):
            # recursion termination condition
            # valid path found, save to path result
            if target == 0:
                res.append(path)
                return
            # invalid path, no need to go deeper
            if target < 0:
                return
            # we are in the [same loop] everytime current dfs returns
            # start from begin, keep checking the rest of the candidates on the [same level]
            for i in range(begin, size):
                dfs(candidates, i, size, path + [candidates[i]], target - candidates[i])
        path = list()
        size = len(candidates)
        res = list()
        dfs(candidates, 0, size, path, target)
        return res
