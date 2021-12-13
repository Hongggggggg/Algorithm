#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from typing import List

class Solution: # 贪心思路
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] >= minPrice and prices[i] <= minPrice + fee: 
                continue
            else: 
                result += prices[i] - minPrice - fee
                minPrice = prices[i] - fee
            print(prices[i], minPrice, result)
        return result
