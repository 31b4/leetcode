class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        sm = prices[0]
        i_sm = 0
        sumprofit = 0
        if len(prices) == 2:
            if prices[0] > prices[1]:
                return 0
            else:
                return prices[1] - prices[0]
        while i < len(prices):
            if prices[i] < sm:
                sm = prices[i]
                i_sm = i
                i+=1
            else:                
                j = i
                prev = prices[j]
                while j < len(prices) and prices[j] >= prev:
                    prev = prices[j]
                    j+=1
                sub_list = prices[i_sm:j]
                i = j-1
                sumprofit += max(sub_list) - min(sub_list)
                print(sub_list)
                i+=1
                if i != len(prices):
                    sm = prices[i]
                    i_sm = i
                else:
                    return sumprofit
        return 0
