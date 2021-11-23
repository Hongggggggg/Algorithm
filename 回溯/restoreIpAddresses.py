#https://leetcode-cn.com/problems/restore-ip-addresses/

class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str):
        '''
        本质切割问题使用回溯搜索法，本题只能切割三次，所以纵向递归总共四层
        因为不能重复分割，所以需要start_index来记录下一层递归分割的起始位置
        添加变量point_num来记录逗号的数量(0,3)
        '''
        self.result.clear()
        if len(s) > 12: return []
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s:str, start_index: int, point_num: int) -> None:
        if point_num == 3:
            if self.is_valid(s, start_index, len(s) - 1):
                self.result.append(s[:])
            return

        #单层递归逻辑
        for i in range(start_index, len(s)):
            if self.is_valid(s, start_index, i):
                s = s[ : i + 1] + '.' + s[i + 1 : ]
                self.backtracking(s, i + 2, point_num + 1)
                s = s[ : i + 1] + s[i + 2 : ]
            else:
                break

    def is_valid(self, s: str, start: int, end: int) -> bool:
        if start > end: return False

        #若数字是0开头则不合法
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start : end + 1]) <= 255:
            return False
        return True
