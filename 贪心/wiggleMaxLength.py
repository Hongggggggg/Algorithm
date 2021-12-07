#https://leetcode-cn.com/problems/wiggle-subsequence/

from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        preC, curC, res = 0, 0, 1
        for i in range(len(nums) - 1):
            curC = nums[i + 1] - nums[i]
            if curC * preC <= 0 and curC != 0:
                res += 1
                preC = curC
        return res
