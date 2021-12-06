#https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key = abs, reverse = True)
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1

        if k > 0:
            nums[-1] *= (-1) ** k
        return sum(nums)