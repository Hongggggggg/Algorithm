#https://leetcode-cn.com/problems/repeated-substring-pattern/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool: 
        length = len(s)
        if length == 0:
            return False

        nxt = [0] * length
        self.getNext(nxt, s)
        if nxt[-1] != -1 and length % (length - (nxt[-1] + 1)) == 0:
            return True
        return False

    def getNext(self, nxt, s):
        nxt[0] = -1
        j = -1
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j + 1]:
                j = nxt[j]
            if s[i] == s[j + 1]:
                j += 1
            nxt[i] = j
        return nxt
