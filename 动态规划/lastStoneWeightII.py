#https://leetcode-cn.com/problems/last-stone-weight-ii/

from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumweight = sum(stones)
        target = sumweight // 2
        dp = [0] * (target + 1)
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return sumweight - 2 * dp[target]
        