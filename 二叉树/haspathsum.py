#https://leetcode-cn.com/problems/path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归
class solution:
    def haspathsum(self, root: TreeNode, targetSum: int) -> bool:
        def isornot(root, targetSum) -> bool:
            if not root.left and not root.right and targetSum == 0:
                return True #遇到叶子节点，并且计数为0
            
            if not root.left and not root.right: 
                return False #遇到叶子节点，计数不为0

            if root.left:
                targetSum -= root.left.val #左节点
                if isornot(root.left, targetSum):
                    return True #递归处理左节点
                targetSum += root.left.val #回溯

            if root.right:
                targetSum -= root.right.val #右节点
                if isornot(root.right, targetSum):
                    return True
                targetSum += root.right.val
            return False
        
        if root == None:
            return False
        else:
            return isornot(root, targetSum - root.val)


#迭代
class solution:
    def haspathsum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = []
        stack.append((root, root.val))

        while stack:
            cur_node, path_sum = stack.pop()

            if not cur_node.left and not cur_node.right and path_sum == targetSum:
                return True

            if cur_node.right: 
                stack.append((cur_node.right, path_sum + cur_node.right.val))    

            if cur_node.left: 
                stack.append((cur_node.left, path_sum + cur_node.left.val))

        return False
