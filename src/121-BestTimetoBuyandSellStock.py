class MySolution:
    def maxProfit(self, prices):
        # tmp profit
        buy = 0
        max_profit = 0
        while buy < len(prices):
            sell = buy + 1
            # there's profit and chance to sell
            while sell < len(prices) and prices[buy] < prices[sell]:
                # update if we can sell at higher price
                max_profit = max(max_profit, prices[sell] - prices[buy])
                # keep looking for higher price to sell
                sell += 1
            # buy on the next day
            buy += 1
        return max_profit


class Solution2:
    def maxProfit(self, prices):
        # assume the lowest price from the beginning
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            # always try to sell at higher price if there's one
            max_profit = max(max_profit, price - min_price)
            # always try to buy at lower price if there's one
            # else current price is lower, we should hold it
            min_price = min(min_price, price)
        return max_profit
