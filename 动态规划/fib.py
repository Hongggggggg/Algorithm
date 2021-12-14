#https://leetcode-cn.com/problems/fibonacci-number/submissions/
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0, 1]
        for i in range(1, n):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[1]