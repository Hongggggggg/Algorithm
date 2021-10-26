#https://leetcode-cn.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归法
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


#迭代法
import collections
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        result = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                result += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


#完全二叉树
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        leftHeight = 0 
        rightHeight = 0
        while left: #求左子树深度
            left = left.left
            leftHeight += 1
        while right:
            right = right.right
            rightHeight += 1
        if leftHeight == rightHeight:
            return (2 << leftHeight) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1