class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minBuy = prices[0]
        for i in range(1,len(prices)):
            print(minBuy)
            minBuy = min(prices[i],minBuy)
            res =  max(res,prices[i] - minBuy)
        return res