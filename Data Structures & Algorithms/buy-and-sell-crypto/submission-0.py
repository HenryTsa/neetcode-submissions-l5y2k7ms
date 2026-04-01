class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        accumulate_prices = [0]*len(prices)
        accumulate_prices[0] = prices[0] 
        for idx in range(1,len(prices)):
            accumulate_prices[idx] = prices[idx] - prices[idx-1]
        #print(accumulate_prices)
        for idx in range(1,len(prices)):
            accumulate_prices[idx] = accumulate_prices[idx-1] + accumulate_prices[idx]
        #print(accumulate_prices)
        res = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                res = max(accumulate_prices[j]-accumulate_prices[i],res)
        #print(res)
        return res