class Solution1:
    def maxProfit(self, prices):
        n = len(prices)
        # DP, only two conditions
        dp = [[0, 0]] * n
        # HOLD CASH on day 0, not buying anything.
        dp[0][0] = 0
        # HOLD STOCK on day 1, BUY stock at prices[0]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            # dp[i] account balance of day i
            # HOLD CASH: dp[i][0] account balance of day i while holding cash
            # SELL stock at price[i] if that INCREASE our balance, meaning SELL at higher price
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # HOLD STOCK: dp[i][1] account balance of day i while holding stock
            # BUY stock at price[i], if that INCREASE our balance, meaning BUY at lower price
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]


class Solution2:
    def maxProfit(self, prices):
        # BUY at price[i-1] SELL at price[i] if there's PROFIT
        profit = 0
        for i in range(1, len(prices)):
            curr = prices[i] - prices[i - 1]
            if curr > 0:
                profit += curr
        return profit
