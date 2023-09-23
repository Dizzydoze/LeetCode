class Solution:
    def fib(self, n: int) -> int:
        ### dynamic programmin(also known as dynamic optimization) is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions - ideally, suing a memory-based data structure.
        # total n+1 numbers [0, n]
        memo = [0, 1] + [0] * (n + 1 - 2)
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]
