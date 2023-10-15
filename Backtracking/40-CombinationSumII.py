class Solution:
    """DFS, Backtracking"""

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, target):
            # use target minus to 0 is better than using sum()
            # recursion termination condition
            # target found, add to result
            if target == 0:
                res.append(path)
                return
            for idx in range(begin, size):
                # KEY: no need to go forward if candidate > target for sorted list
                if candidates[idx] > target:
                    break
                # KEY: skip duplication
                if idx > begin and candidates[idx] == candidates[idx - 1]:
                    continue
                # KEY: for current idx, check the rest of the candidates match or not
                dfs(idx + 1, path + [candidates[idx]], target - candidates[idx])

        # sort to avoid duplicates and break once the num is bigger than target
        candidates.sort()
        size = len(candidates)
        res = list()
        dfs(0, [], target)
        return res
