#https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []
        r = float("inf")
        def buildList(root):
            if not root: return None
            if root.left: buildList(root.left) #左
            res.append(root.val) #中
            if root.right: buildList(root.right) #右
            return res

        buildList(root)
        for i in range(len(res) - 1):
            r = min(abs(res[i] - res[i + 1]), r)

        return r

#迭代
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        cur = root
        pre = None
        result = float('inf')
        while cur or stack:
            if cur: #访问到最底层
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre: #当前节点和前节点的值的差值
                    result = min(result, cur.val - pre.val)
                pre = cur
                cur = cur.right

        return result

