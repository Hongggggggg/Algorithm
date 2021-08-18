#https://leetcode-cn.com/problems/squares-of-a-sorted-array/


def Sorted_Squares(nums):
    length = len(nums)
    left, right = 0, len(nums) - 1
    rst = [-1] * length
    pos = length - 1
    print(rst)
    while left <= right: #等于的时候也要进行一轮操作
        left_value = nums[left] ** 2
        right_value = nums[right] ** 2
        if left_value > right_value:
            rst[pos] = left_value
            left += 1
        else:
            rst[pos] = right_value
            right -= 1
        pos -= 1
    return rst 

print(Sorted_Squares([-14,-7,-3,2,3,11,12]))
