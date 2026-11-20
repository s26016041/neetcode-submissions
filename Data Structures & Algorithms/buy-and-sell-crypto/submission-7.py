class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        buyPrice= prices[0]

        for p in prices:
            if buyPrice > p:
                buyPrice = p
            elif p - buyPrice  > output:
                output =  p - buyPrice  

        return output