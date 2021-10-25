#https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

#递归
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root :
            return 0
        depth = 0
        for i in range(len(root.children)):
            depth = max(depth, self.maxDepth(root.children[i]))
        return depth + 1

#迭代法：
import collections
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        depth = 0 #记录深度
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.popleft()
                for j in range(len(node.children)):
                    if node.children[j]:
                        queue.append(node.children[j])
        return depth