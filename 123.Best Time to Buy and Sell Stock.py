class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1, sell1 = float('-inf'), 0
        buy2, sell2 = float('-inf'), 0

        for price in prices:
            buy1 = max(buy1, -price)          # first buy
            sell1 = max(sell1, buy1 + price)  # first sell
            buy2 = max(buy2, sell1 - price)   # second buy
            sell2 = max(sell2, buy2 + price)  # second sell

        return sell2
