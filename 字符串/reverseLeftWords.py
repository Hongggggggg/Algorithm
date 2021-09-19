#https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        def reverse_sub(li, left, right):
            while left < right:
                li[left], li[right] = li[right], li[left]
                left += 1
                right -= 1

        res = list(s)
        end = len(res) - 1
        reverse_sub(res, 0, n - 1)
        reverse_sub(res, n, end)
        reverse_sub(res, 0, end)
        return ''.join(res)
