#https://leetcode-cn.com/problems/combination-sum/

class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def combinationSum(self, candidates, target: int):
        self.path.clear()
        self.paths.clear()
        candidates.sort() #为了剪枝需要提前进行排序
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates, target, sum_, start_index):
        if sum_ == target:
            self.paths.append(self.path[:])
            return

        #单层递归逻辑
        for i in range(start_index, len(candidates)):
            if sum_ + candidates[i] > target: #剪枝
                return
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i)
            sum_ -= candidates[i]
            self.path.pop()

