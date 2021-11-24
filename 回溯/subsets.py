#https://leetcode-cn.com/problems/subsets/

class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def subsets(self, nums):
        self.path.clear()
        self.paths.clear()
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums, startIndex):
        self.paths.append(self.path[:])
        if startIndex >= len(nums):
            return

        for i in range(startIndex, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()
            