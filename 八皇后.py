#n为行数, record为所有答案
def dfs(n, queens, record):
    # 记录答案与控制递归深度
    if n >= 4:
        # 由于Python当中传递的是引用，所以这里需要copy
        # 否则当后面queens pop的时候，会影响record当中记录的值
        record.append(queens.copy())
        return
    #i表示列
    for i in range(4):
        # 判断是否同列
        if i in queens:
            continue
        # 判断是否同对角线
        flag = False
        for j in range(len(queens)):
            if abs(n - j) == abs(i - queens[j]):
                flag = True
                break
        if flag:
            continue
        # 递归与回溯
        queens.append(i)
        dfs(n+1, queens, record)
        queens.pop()

queens = []
record = []
dfs(0, queens, record)
print(record)
