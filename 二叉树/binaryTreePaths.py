#https://leetcode-cn.com/problems/binary-tree-paths/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        path = ''
        result = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result

    def traversal(self, cur: TreeNode, path: str, result) -> None:
        path += str(cur.val)
        #若当前节点为叶子节点，直接输出
        if not cur.left and not cur.right:
            result.append(path)
        
        if cur.left:
            # + '->'是隐藏回溯
            self.traversal(cur.left, path + '->', result)

        if cur.right:
            self.traversal(cur.right, path + '->', result)


root_left = TreeNode(2)
root_right = TreeNode(3)
root = TreeNode(1, root_left, root_right)


a = Solution()
print(a.binaryTreePaths(root))