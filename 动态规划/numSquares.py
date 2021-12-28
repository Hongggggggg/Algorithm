#https://leetcode-cn.com/problems/perfect-squares/
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n):
            if i * i > n:
                break
            num = i * i
            for j in range(num, n + 1):
                dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]