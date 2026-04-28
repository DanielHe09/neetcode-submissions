class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max = 0

        for price in prices:
            for num in range(prices.index(price)+1, len(prices)):
                if (prices[num]-price)>max:
                    max = prices[num]-price

        return max