def MaxProfit(prices):
    result = 0
    for i in range(1, len(prices)):
        result += max(prices[i] - prices[i - 1], 0)
    return result

print(MaxProfit([1,2,3,4,5]))