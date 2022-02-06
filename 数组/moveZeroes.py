#https://leetcode-cn.com/problems/move-zeroes/submissions/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fastIndex, slowIndex = 0, 0
        while fastIndex < len(nums):
            if nums[fastIndex] != 0:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
            fastIndex += 1

        for i in range(slowIndex, len(nums)):
            nums[i] = 0 
