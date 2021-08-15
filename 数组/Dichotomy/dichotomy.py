#左闭右开

# def binary_search(a, v):
#     l, r = 0, len(a)
#     while l + 1 < r:
#         m = (l + r) // 2
#         if a[m] <= v:
#             l = m
#         else:
#             r = m
#     # 通过a[l] == v判断v不存在与a数组当中的情况
#     return l,r

#https://leetcode-cn.com/problems/binary-search/
#左闭右闭
def binary_search(li, target):
    left = 0
    right = len(li) - 1
    while(left <= right): #要包含等号是因为li如果只有一个元素，left和right就是相等的，此时也是需要执行下面的操作
        middle = (right + left) // 2
        if target == li[middle]: #与middle比较必须放在最开始，因为middle有可能与left相等
            return middle
        elif target < li[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1


nums = [1]
print(binary_search(nums, 1))

