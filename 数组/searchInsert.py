#https://leetcode-cn.com/problems/search-insert-position/submissions/
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        index = -1
        while(left <= right):
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle - 1

            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return left