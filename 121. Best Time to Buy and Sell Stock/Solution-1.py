import math


class Solution:
    def maxProfit(self, prices: list[int]) -> float | int:
        cheapest_so_far = math.inf
        max_profit = 0
        for price in prices:
            if price < cheapest_so_far:
                cheapest_so_far = price
            elif price - cheapest_so_far > max_profit:
                max_profit = price - cheapest_so_far
        return max_profit
