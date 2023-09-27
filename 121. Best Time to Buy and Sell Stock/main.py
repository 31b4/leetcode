class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        i = 0
        if len(prices) > 1:
            max_price = max(prices[1:])
        else:
            max_price = max(prices)

        while i < len(prices):
            if max_price == 0:
                break
            if max_price == prices[i] and i < len(prices)-1:
                max_price = max(prices[i+1:])
                if max_price == min(prices[i+1:]):
                    break
            if max_price - prices[i] > max_profit:
                max_profit = max_price - prices[i]
            i+=1
        return max_profit
