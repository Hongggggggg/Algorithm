#https://leetcode-cn.com/problems/combination-sum-iv/
class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for j in range(1, target + 1):
            for i in nums:
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[-1]