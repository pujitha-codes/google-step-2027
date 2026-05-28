class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price # lowest price inka kanukkuntam
            elif price - min_price > max_profit:
                max_profit = price - min_price # profit check chestam

        return max_profit
