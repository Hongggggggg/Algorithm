#https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#递归法-有返回值
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 返回更新后的以当前root为根节点的新树，方便用于更新上一层的父子节点关系链

        #Base Case
        if not root: return TreeNode(val)

        #单层递归逻辑：
        if val < root.val:
            #将val插入至当前root的左子树中合适的位置
            #并更新当前的root的左子树为包含目标val的新左子树
            root.left = self.insertIntoBST(root.left, val)

        if root.val < val:
            # 将val插入至当前root的右子树中合适的位置
            # 并更新当前root的右子树为包含目标val的新右子树
            root.right = self.insertIntoBST(root.right, val)

        return root


#递归法-无返回值
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        parent = None

        def __traverse(cur: TreeNode, val: int) -> None:
            #在函数运行的同时把新节点插入到该被插入的地方
            nonlocal parent
            if not cur:
                new_node = TreeNode(val)
                if parent.val < val:
                    parent.right = new_node
                else:
                    parent.left = new_node
                return 

            parent = cur #parent的作用只有运行到上面的if not cur才会发挥出来
            if cur.val < val:
                __traverse(cur.right, val)
            else:
                __traverse(cur.left, val)
            return
        __traverse(root, val)
        return root


#迭代法
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        parent = None
        cur = root

        #用while循环不断地找新节点的parent
        while cur:
            if cur.val < val:
                parent = cur
                cur = cur.right
            elif cur.val > val:
                parent = cur
                cur = cur.left
        
        # 运行到这意味着已经跳出上面的while循环, 
        # 同时意味着新节点的parent已经被找到.
        # parent已被找到, 新节点已经ready. 把两个节点黏在一起就好了. 
        if parent.val > val: 
            parent.left = TreeNode(val)
        else: 
            parent.right = TreeNode(val)
        return root