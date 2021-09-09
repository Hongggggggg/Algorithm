#https://leetcode-cn.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target: int):
        records = dict()

        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx]
