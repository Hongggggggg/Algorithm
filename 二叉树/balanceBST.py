#https://leetcode-cn.com/problems/balance-a-binary-search-tree/

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = []
        def traversal(cur: TreeNode):
            if not cur: return 
            traversal(cur.left)
            res.append(cur.val)
            traversal(cur.right)

        def getTree(nums: List, left, right):
            if left > right: return
            middle = left + (right - left) // 2
            root = TreeNode(nums[middle])
            root.left = getTree(nums, left, middle - 1)
            root.right = getTree(nums, middle + 1, right)
            return root
        
        traversal(root)
        return getTree(res, 0, len(res) - 1)
        