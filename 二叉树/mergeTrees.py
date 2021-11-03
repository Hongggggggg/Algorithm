#https://leetcode-cn.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        #递归终止条件
        #但凡有一个节点为空，就立刻返回另一个，如果另一个也为None，则直接返回None
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val #中
        root1.left = self.mergeTrees(root1.left, root2.left) #左
        root1.right = self.mergeTrees(root1.right, root2.right) #右

        return root1

#迭代法
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        import collections
        queue = collections.deque()
        queue.append(root1)
        queue.append(root2)

        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()

            #更新queue
            #只有两个节点都有左节点的时候，再往queue里放
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)

            #只有两个节点都有右节点的时候，再往queue里放
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)

            #更新当前节点，同时改变当前节点的左右孩子
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right

        return root1
