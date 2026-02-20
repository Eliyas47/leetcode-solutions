class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        # Initialize states
        hold = -prices[0]   # Max profit when holding a stock
        sold = 0            # Max profit when just sold a stock
        rest = 0            # Max profit when in cooldown or resting

        for i in range(1, n):
            prev_hold, prev_sold, prev_rest = hold, sold, rest

            # Either keep holding or buy today (from rest state)
            hold = max(prev_hold, prev_rest - prices[i])
            # Sell today (must have been holding yesterday)
            sold = prev_hold + prices[i]
            # Rest today (either from rest or sold yesterday)
            rest = max(prev_rest, prev_sold)

        # Max profit is either in sold or rest state
        return max(sold, rest)
