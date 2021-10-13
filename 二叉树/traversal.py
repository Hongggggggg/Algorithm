#前序遍历(中左右)
class Solution:
    def preorderTraversal(self, root):
        result = []

        def traversal(root):
            if root == None:
                return
            result.append(root.val) #中
            traversal(root.left) #左
            traversal(root.right) #右
        
        traversal(root)
        return result

#中序遍历(左中右)
class Solution:
    def preorderTraversal(self, root):
        result = []

        def traversal(root):
            if root == None:
                return
            traversal(root.left) #左
            result.append(root.val) #中
            traversal(root.right) #右
        
        traversal(root)
        return result


#后序遍历(左右中)
class Solution:
    def preorderTraversal(self, root):
        result = []

        def traversal(root):
            if root == None:
                return
            traversal(root.left) #左
            traversal(root.right) #右
            result.append(root.val) #中

        traversal(root)
        return result