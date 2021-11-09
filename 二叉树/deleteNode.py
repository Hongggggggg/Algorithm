#https://leetcode-cn.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return root #第一种情况：没找到删除的节点，遍历到空节点直接返回了
        if root.val == key:
            if not root.left and not root.right: #第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
                del root
                return None

            if not root.left and root.right: #第三种情况：其左孩子为空，右孩子不为空，删除节点，右孩子补位 ，返回右孩子为根节点
                tmp = root
                root = root.right
                del tmp
                return root
            
            if root.left and not root.right: #第四种情况：其右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
                tmp = root
                root = root.left
                del tmp
                return root
            else:  #第五种情况：左右孩子节点都不为空，则将删除节点的左子树放到删除节点的右子树的最左面节点的左孩子的位置
                v = root.right
                while v.left:
                    v = v.left
                v.left = root.left
                tmp = root
                root = root.right 
                del tmp
                return root
        if root.val > key: root.left = self.deleteNode(root.left, key) #左递归
        if root.val < key: root.right = self.deleteNode(root.right, key) #右递归
        return root