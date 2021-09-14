def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while li[right] >= tmp and left < right:
            right -= 1
        li[left] = li[right]
        
        while li[left] <= tmp and left < right:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right: #至少含有两个元素
        middle = partition(li, left, right)
        quick_sort(li, left, middle - 1)
        quick_sort(li, middle + 1, right)
    print(li)
    
a = [5, 5, 4, 6, 6, 5, 7, 7, 9, 1, 2, 5]
quick_sort(a, 0, len(a) - 1)
