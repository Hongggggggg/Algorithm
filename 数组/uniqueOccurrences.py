#https://leetcode-cn.com/problems/unique-number-of-occurrences/
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_1 = [0] * 2001
        for i in range(len(arr)):
            hash_1[arr[i] + 1000] += 1

        hash_2 = [0] * 1000
        for i in range(len(hash_1)):
            if hash_1[i] != 0:
                if hash_2[hash_1[i]] == 0:
                    hash_2[hash_1[i]] = 1
                else:
                    return False
        return True

a = Solution()
print(a.uniqueOccurrences([1,2,2,1,1,3]))
            



