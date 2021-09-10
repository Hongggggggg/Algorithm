#https://leetcode-cn.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        arr = [0] * 26
        ascii_a = ord('a')
        for x in magazine:
            arr[ord(x) - ascii_a] += 1

        for x in ransomNote:
            if arr[ord(x) - ascii_a] == 0:
                return False
            else:
                arr[ord(x) - ascii_a] -= 1
        
        return True
