#https://leetcode-cn.com/problems/sort-array-by-parity-ii/submissions/
from pip import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        oddIndex = 1
        for i in range(0, len(nums) - 1, 2):
            if(nums[i] % 2 == 1):
                while(nums[oddIndex] % 2 != 0): oddIndex += 2
                nums[i], nums[oddIndex] = nums[oddIndex], nums[i]
        return nums