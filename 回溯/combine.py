#https://leetcode-cn.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int):
        res = []

        path = []
        def backtrack(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            
            #for i in range(startIndex, n + 1):
            for i in range(startIndex, n - (k - len(path)) + 2): #枝剪
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()
        backtrack(n, k, 1)
        return res