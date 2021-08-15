#https://leetcode-cn.com/problems/remove-element/

def rm_element(li, value):
    j = 0 #慢指针
    for i in range(len(li)): #i为快指针
        if li[i] != value: #快指针遇到value不与慢指针交换，直接前进一步
            li[j] = li[i] #先交换，再+1
            j += 1
    return j, li

test_li = [0,1,2,2,3,0,4,2,3,4,5,6]

print(rm_element(test_li, 2))

