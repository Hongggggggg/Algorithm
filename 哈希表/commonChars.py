#https://leetcode-cn.com/problems/find-common-characters/
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        result = []
        hash = [0] * 26
        for i, c in enumerate(words[0]):
            hash[ord(c) - ord('a')] += 1

        for i in range(1, len(words)):
            hashOtherStr = [0] * 26

            for j in range(len(words[i])):
                hashOtherStr[ord(words[i][j]) - ord('a')] += 1

            for k in range(26):
                hash[k] = min(hash[k], hashOtherStr[k])

        for i in range(26):
            while hash[i] != 0:
                result.extend(chr(i + ord('a')))
                hash[i] -= 1
        return result
