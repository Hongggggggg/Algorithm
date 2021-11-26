#https://leetcode-cn.com/problems/increasing-subsequences/

class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def findSubsequences(self, nums):
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums, start_index):
        if len(self.path) >= 2:
            self.paths.append(self.path[:])

        #可省略，索引最多到len(nums)
        if start_index >= len(nums):
            return 

        # 单层递归逻辑
        # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
        usage_list = [False] * 201  # 使用列表去重，题中取值范围[-100, 100]

        for i in range(start_index, len(nums)):
            #若当前元素值小于前一个时或者曾经用过，则跳入下一循环
            if (self.path and nums[i] < self.path[-1]) or usage_list[nums[i]+100] == True:
                continue

            usage_list[nums[i] + 100] = True
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()




