class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftmin=list(accumulate(prices,min))
        profit=0
        for i in range(len(prices)):
            if prices[i]-leftmin[i]>profit:
                profit = prices[i]-leftmin[i]
        return profit