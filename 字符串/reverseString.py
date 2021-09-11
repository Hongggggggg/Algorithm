#https://leetcode-cn.com/problems/reverse-string/
class Solution:
    def reverseString(self, s) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

a = Solution()
print(a.reverseString(['a','b','c','d']))
