#https://leetcode-cn.com/problems/target-sum/
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumValue = sum(nums)
        if abs(target) > sumValue or (sumValue + target) % 2 == 1: return 0
        bagSize = (sumValue + target) // 2
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bagSize]

a = Solution()
print(a.findTargetSumWays([100], -200))
