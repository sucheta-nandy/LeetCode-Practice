class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price, best_profit = float("inf"), 0
        for price in prices:
            profit = price - lowest_price
            best_profit = max(profit, best_profit)
            lowest_price = min(price, lowest_price)
        return best_profit
