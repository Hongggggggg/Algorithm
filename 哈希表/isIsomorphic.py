#https://leetcode-cn.com/problems/isomorphic-strings/
from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = defaultdict(str)
        dict_t = defaultdict(str)

        if(len(s) != len(t)): return False

        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = t[i]

            if t[i] not in dict_t:
                dict_t[t[i]] = s[i]

            if dict_s[s[i]] != t[i] or dict_t[t[i]] != s[i]:
                return False

        return True
        