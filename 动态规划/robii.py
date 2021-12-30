#https://leetcode-cn.com/problems/word-break/
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if(n := len(nums)) == 0:
            return 0
        if n == 1:
            return nums[0]
        
        result1 = self.robRange(nums, 0, n - 2)
        result2 = self.robRange(nums, 1, n - 1)
        return max(result1, result2)

    def robRange(self, nums: List[int], start: int, end: int) -> int:
        if end == start: return nums[start]
        dp = [0] * len(nums)
        dp[start] = nums[start]
        dp[start + 1] = max(nums[start], nums[start + 1])
        for i in range(start + 2, end + 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[end]
