#https://leetcode-cn.com/problems/combination-sum-ii/

class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def combinationSum2(self, candidates, target: int):
        self.paths.clear()
        self.path.clear()
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates, target, sum_, start_index):
        if sum_ == target:
            self.paths.append(self.path[:])
            return

        #单层递归逻辑
        for i in range(start_index, len(candidates)):
            if sum_ + candidates[i] > target:
                return

            #跳过同一树层使用过的元素
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue

            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i + 1)
            self.path.pop()
            sum_ -= candidates[i]
