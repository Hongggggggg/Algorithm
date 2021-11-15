#https://leetcode-cn.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []
        path = []
        def findallPath(n, k, sum, startIndex):
            if sum > n: return #剪枝
            if sum == n and len(path) == k:
                return res.append(path[:])
            for i in range(startIndex, 9 - (k - len(path)) + 2):
                path.append(i)
                sum += i
                findallPath(n, k, sum, i + 1)
                sum -= i
                path.pop()
            
        findallPath(n, k, 0, 1)
        return res