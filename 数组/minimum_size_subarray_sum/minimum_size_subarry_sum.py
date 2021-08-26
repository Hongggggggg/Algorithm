#https://leetcode-cn.com/problems/minimum-size-subarray-sum/
def minSubArrayLen(nums, value):
    length = len(nums)
    res = length + 1
    sum = 0
    win_left = 0
    for win_right in range(length):
        sum += nums[win_right]
        while sum >= value:
            sum -= nums[win_left]
            res = min(res, win_right - win_left + 1)
            win_left += 1
    return 0 if res > length else res


nums = [2, 3, 1, 2, 4, 3, 1, 2, 3, 7]
print(minSubArrayLen(nums, 7))
