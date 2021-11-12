#https://leetcode-cn.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.pre = 0

    def convertBST(self, root):
        self.traversal(root)
        return root

    def traversal(self, root):
        if not root:
            return None
 
        self.traversal(root.right) #右
        root.val += self.pre #中
        self.pre = root.val
        self.traversal(root.left) #左
