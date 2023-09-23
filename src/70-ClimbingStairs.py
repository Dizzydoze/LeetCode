class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        # memory storge, [0, n] -> n + 1 elements
        # 0 step, 1 way; 1 step, 1 way
        memo = [0] * (n + 1)
        memo[0] = 1
        memo[1] = 1
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]


class Solution2:
    """
    reduce the space to only 3 slots, pop out the oldest after adding the new one.
    """
    def climbStairs(self, n: int) -> int:
        memo = [1, 1]
        for i in range(2, n + 1):
            memo.append(memo[0] + memo[1])
            memo.pop(0)
        return memo[1]
