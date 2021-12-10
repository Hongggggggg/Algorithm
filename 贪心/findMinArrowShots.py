#https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0
        points.sort(key = lambda x: x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]: #相邻的气球不挨着
                result += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1]) #更新重叠气球最小右边界
        return result