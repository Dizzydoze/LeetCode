class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Greedy
        # Pretend to buy on Day 0 with cost = price[0] + fee
        buy = prices[0] + fee
        profit = 0
        for i in range(1, len(prices)):  # Start from Day 1 to compare prices
            if prices[i] + fee < buy:    # if buying on Day i is cheaper
                buy = prices[i] + fee    # we will buy on Day i instead
            elif prices[i] > buy:        # Profit exists, we should sell it
                profit += prices[i] - buy   # KEY POINT: Not sure if it is the highest price to sell
                buy = prices[i]             # Pretend to sell it at price on Day i
        return profit                       # Save the price we sold as a new [buy], if there's indeed a higher price
                                            # [Extra Profit] we get from the [higher price] is still prices[i] - buy.
