#https://leetcode-cn.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i]表示爬到第i级楼梯的种数， (1, 2) (2, 1)是两种不同的类型
        dp = [0] * (n + 1)
        dp[0] = 1
        m = 2 #最多可以走几步
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i >= j:
                    dp[i] += dp[i - j]
        return dp[-1]
