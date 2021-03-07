def WiggleMaxLength(li):
    if len(li) <= 1:
        return len(li)
    
    cur_diff = 0 #当前一对差值
    pre_diff = 0 #前一对差值
    result = 1 #记录峰值个数

    for i in range(1, len(li)):
        cur_diff = li[i] - li[i - 1]
        if (cur_diff > 0 and pre_diff <= 0) or (pre_diff >= 0 and cur_diff < 0):
            result += 1
            pre_diff = cur_diff
    return result


print(WiggleMaxLength([1,7,4,9,2,5]))
