
def maxSubArray(nums):
    result = 0
    count = 0
    for i in nums:
        count += i

        if count > result: #取区间累计的最大值（相当于不断确定最大子序终止位置）
            result = count

        if count <= 0: #相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
            count = 0
    return result

print(maxSubArray([-2,1,-3,4,-1,2,1,-3,4]))