#https://leetcode-cn.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        ascii_a = ord('a')
        for i in range(len(s)):
            record[ord(s[i]) - ascii_a] += 1
        
        for i in range(len(t)):
            record[ord(t[i]) - ascii_a] -= 1
        
        for i in range(26):
            if record[i] != 0:
                return False
        return True

a = Solution()
print(a.isAnagram('abcdefg', 'cbadefg'))
