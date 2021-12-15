#https://leetcode-cn.com/problems/unique-paths-ii/
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        if obstacleGrid[0][0] == 1: return 0

        #第一行
        for i in range(col):
            if obstacleGrid[0][i] == 1:
                break
            else:
                 dp[0][i] = 1

        #第一列
        for i in range(row):
            if obstacleGrid[i][0] == 1:
                break
            else:
                 dp[i][0] = 1
        print(dp)
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
