#https://leetcode-cn.com/problems/assign-cookies/

from typing import List


class Solution:
    # 思路1：优先考虑饼干
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)):
            if res < len(g) and s[i] >= g[res]: #从小饼干开始喂
                res += 1
        return res


class Solution:
    # 思路2：优先考虑胃口
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        start, count = len(s) - 1, 0
        for index in range(len(g) - 1, -1, -1):
            if start >= 0 and g[index] <= s[start]:
                start -= 1
                count += 1
        return count
        