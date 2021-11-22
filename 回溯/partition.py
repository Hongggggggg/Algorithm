#https://leetcode-cn.com/problems/palindrome-partitioning/

class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def partition(self, s: str):
        '''
        递归用于纵向遍历
        for循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到一种方法
        类似组合问题，为了不重复切割同一位置，需要start_index来做标记下一轮递归的起始位置(切割线)
        '''
        self.path.clear()
        self.paths.clear()
        self.backtracking(s, 0)
        return self.paths

    def backtracking(self, s: str, start_index: int) -> None:
        if start_index >= len(s):
            self.paths.append(self.path[:])
            return

        #单层递归逻辑
        for i in range(start_index, len(s)):
            temp = s[start_index : i + 1]
            if temp == temp[::-1]: #判断是否为回文串
                self.path.append(temp)
                self.backtracking(s, i + 1)
                self.path.pop()
            else:
                continue