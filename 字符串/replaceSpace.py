#https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
class Solution:
    def replaceSpace(self, s: str) -> str:
        counter = s.count(' ')
        res = list(s)
        res.extend([' '] * counter * 2)

        left, right = len(s) - 1, len(res) - 1
        while left < right:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                res[right - 2 : right + 1] = '%20'
                right -= 3
            left -= 1
        return ''.join(res)
