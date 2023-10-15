class Solution:
    """
                DFS, Backtracking
                    (0, 0, '')
                        |
                    (1, 0, '(')
                    /           \
            (2, 0, '((')      (1, 1, '()')
                /                 \
        (2, 1, '(()')           (2, 1, '()(')
            /                       \
    (2, 2, '(())')                (2, 2, '()()')
           |	                          |
    res.append('(())')             res.append('()()')
    """
    def generateParenthesis(self, n: int) -> List[str]:
        # left: number of left parentheses
        # right: number of right parentheses
        # s: current combination string
        def dfs(left, right, s):
            # recursion termination condition
            if len(s) == n * 2:
                res.append(s)
                return
            # There are still left parentheses to add
            # add one '(' to combination, and count left += 1, keep going deeper
            if left < n:
                dfs(left+1, right, s + '(')
            # There are still right parentheses to add
            # add one ')' to combination, and count right += 1, keep going deeper
            if right < left:
                dfs(left, right + 1, s + ')')
        s = ''
        res = list()
        dfs(0, 0, s)
        return res
