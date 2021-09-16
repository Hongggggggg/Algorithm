#https://leetcode-cn.com/problems/reverse-string-ii/
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        1. 使用range(start, end, step)来确定需要调换的初始位置
        2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
        3. 用切片整体替换，而不是一个个替换.
        """
        def reverse_substr(sub_str):
            left, right = 0, len(sub_str) - 1
            while left < right:
                sub_str[left], sub_str[right] = sub_str[right], sub_str[left]
                left += 1
                right -= 1
            return sub_str

        res = list(s)

        for cur in range(0, len(s), 2 * k):
            print(cur, cur + k)
            res[cur: cur + k] = reverse_substr(res[cur: cur + k])
        
        return ''.join(res)


a = Solution()
print(a.reverseStr("abcdefgh", 3))

