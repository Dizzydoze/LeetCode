class Solution:
    def tribonacci(self, n: int) -> int:
        # DP, same as Fibonacci
        res = [0, 1, 1]
        if n < 3:
            return res[n]
        for _ in range(3, n + 1):  # O(1) space
            res.append(sum(res))   # new sum(i-3, i-2, i-1) added to the end
            res.pop(0)             # remove leftmost ele to save space
        return res[-1]
