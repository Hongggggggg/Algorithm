#https://leetcode-cn.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#递归
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)

        if root.val < val:
            return self.searchBST(root.right, val)


#迭代
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return root
