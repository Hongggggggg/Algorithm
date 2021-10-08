#https://leetcode-cn.com/problems/sliding-window-maximum/
class MyQueue:
    def __init__(self) -> None:
        self.queue = []

    #每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    #同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0) 

    #如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    #这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        que = MyQueue()
        result = []
        for i in range(k): #先把前面k个元素放进队列
            que.push(nums[i])
        result.append(que.front()) #记录前k个元素的最大值
        for i in range(k, len(nums)):
            que.pop(nums[i - k])
            que.push(nums[i])
            result.append(que.front())
        return result

