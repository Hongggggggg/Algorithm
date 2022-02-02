#https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = nums[:]
        res.sort()
        hash = [0] * 101
        for i in range(len(res) - 1, -1, -1):
            hash[res[i]] = i
        
        for i in range(len(nums)):
            res[i] = hash[nums[i]]

        return res
            
        