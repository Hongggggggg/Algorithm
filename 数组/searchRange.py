from cgi import print_directory
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while(left <= right):
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    return middle
            return -1
        pos = binarySearch(nums, target)
        if pos == -1:
            return [-1, -1]

        print(pos)
        print_directory
        left, right = pos, pos
        while(left > 0 and nums[left] == target): left -= 1
        while(right < len(nums) and nums[right] == target): right += 1
        print(left + 1, right - 1)

a = Solution()
a.searchRange([5,7,7,8,8,10], 8)
