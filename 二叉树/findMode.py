#https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/solution/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归
class Solution:
    def __init__(self) -> None:
        self.pre = TreeNode()
        self.count = 0
        self.max_count = 0
        self.result = []

    def findMode(self, root: TreeNode):
        if not root: return None
        self.search_BST(root)
        return self.result

    def search_BST(self, cur: TreeNode):
        if not cur: return None
        self.search_BST(cur.left) #左
        if not self.pre: #第一个节点
            self.count = 1
        elif self.pre.val == cur.val: # 与前一个节点数值相同
            self.count += 1
        #与前一个节点数值不相同
        else:
            self.count = 1

        self.pre = cur

        if self.count == self.max_count:
            self.result.append(cur.val)
        
        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [cur.val] #清空self.result，确保result之前的元素都失效

        self.search_BST(cur.right)
        


#迭代
class Solution:
    def findMode(self, root: TreeNode):
        stack = []
        cur = root
        pre = None
        maxCount, count = 0, 0
        res = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else: #逐一处理节点
                cur = stack.pop()
                if pre == None: #第一个节点
                    count = 1
                elif pre.val == cur.val: #与前一个节点数值相同
                    count += 1
                else:
                    count = 1

                if count == maxCount:
                    res.append(cur.val)
                if count > maxCount:
                    maxCount = count
                    res.clear()
                    res.append(cur.val)
                
                pre = cur
                cur = cur.right
        return res
