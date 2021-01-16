#左闭右开
'''
def binary_search(a, v):
    l, r = 0, len(a)
    while l + 1 < r:
        m = (l + r) // 2
        if a[m] <= v:
            l = m
        else:
            r = m
    # 通过a[l] == v判断v不存在与a数组当中的情况
    return l,r
'''
#闭区间

def binary_search(a, v):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == v:
            return m
        if a[m] < v:
            l = m + 1
        else:
            r = m - 1
    # 表示不存在
    return -1


nums = [1,2,3,4,5,6,7,8,9,10,11,12]

print(binary_search(nums, 13))



