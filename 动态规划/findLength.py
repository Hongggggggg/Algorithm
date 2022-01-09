#https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
from typing import List


'''
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        result = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
        return result
'''

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [0] * (len(B) + 1)
        result = 0
        for i in range(1, len(A) + 1):
            for j in range(len(B), 0, -1):
                if A[i - 1] == B[j - 1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0
                result = max(result, dp[j])
        return result
        