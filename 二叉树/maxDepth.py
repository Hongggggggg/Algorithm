#https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
#迭代法
class solution:
    def maxDepth(self, root) -> int:
        return self.getdepth(root)

    def getdepth(self, node):
        if not node:
            return 0
        leftdepth = self.getdepth(node.left) #左
        rightdepth = self.getdepth(node.right) #右
        depth = 1 + max(leftdepth, rightdepth) #中
        return depth

#迭代法精简版
class solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


#迭代法
import collections
class solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        depth = 0 #记录深度
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


