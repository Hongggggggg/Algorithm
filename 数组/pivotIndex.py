#https://leetcode-cn.com/problems/find-pivot-index/
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            left_sum += nums[i]
            if sum_ - left_sum + nums[i] == left_sum:
                return i
        
        return -1