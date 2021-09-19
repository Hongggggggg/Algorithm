#https://leetcode-cn.com/problems/reverse-words-in-a-string/
class Solution:
    #删除多余空格
    def removeExtraSpaces(self, s):
        slowIndex, fastIndex = 0, 0
        strLen = len(s)
        #移除字符串开头多余的空格
        while(strLen > 0 and fastIndex < strLen and s[fastIndex] == ' '):
            fastIndex += 1
        
        #移除字符串中间多余的空格
        for i in range(fastIndex, strLen):
            if ((i - 1 > 0) and (s[i - 1] == s[i] == ' ')):
                continue
            else:
                s[slowIndex] = s[i]
                slowIndex += 1

        #移除字符串末尾的空格
        while s[slowIndex - 1] == ' ':
            slowIndex -= 1

        return s[:slowIndex]
    
    #翻转字符串
    def reverse_string(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverse_each_word(self, s):
        start, end = 0, 0
        n = len(s)
        while start < n:
            while end < n and s[end] != ' ':
                end += 1
            print(s[start:end])
            s[start:end] = self.reverse_string(s[start:end])
            print(s[start:end])
            start = end + 1
            end += 1
        return s

    
    def reverseWords(self, s: str) -> str:
        ret = list(s)
        print(ret)
        ret = self.removeExtraSpaces(ret)
        print(ret)
        ret = self.reverse_string(ret)
        print(ret)
        ret = self.reverse_each_word(ret)
        print(ret)
        return ''.join(ret)

a = Solution()
str_test = "  abcd [0000]   [1234] efga    "
print(str_test)
print(a.reverseWords(str_test))
