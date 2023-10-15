class Solution:
    def minSteps(self, n: int) -> int:
        # DP
        dp = [inf] * (n + 1)
        dp[1] = 0
        for curr in range(2, n + 1):
            for screen in range(1, curr):
                # for current num 'curr', 'screen' is a factor of 'curr', curr = m * screen
                if curr % screen == 0:
                    # dp[screen]: total steps we need to get num 'screen'
                    # dp[screen] + 1: copy screen number, cost 1 step
                    # curr//screen - 1: we need m = curr//screen 'screen' to reach curr,
                    # we already got 1 'screen', we need m = curr//screen - 1 more.
                    dp[curr] = min(dp[curr], dp[screen] + 1 + curr // screen - 1)
        return dp[-1]
