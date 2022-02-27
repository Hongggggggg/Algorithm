#https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        path = []
        def backtrace(root):
            nonlocal res
            if not root: return 
            path.append(root.val)
            if not root.left and not root.right:
                res += get_sum(path)

            if root.left:
                backtrace(root.left)

            if root.right:
                backtrace(root.right)
            path.pop()

        def get_sum(arr):
            s = 0
            for i in range(len(arr)):
                s = s * 10 + arr[i]
            return s

        backtrace(root)
        return res