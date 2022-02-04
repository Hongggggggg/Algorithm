#https://leetcode-cn.com/problems/valid-mountain-array/submissions/
from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left, right = 0, len(arr) - 1
        while (left < right and arr[left] < arr[left + 1]):
            left += 1

        while (left < right and arr[right - 1] > arr[right]):
            right -= 1

        if (left != right or left == 0 or right == len(arr) - 1):
            return False
        else:
            return True