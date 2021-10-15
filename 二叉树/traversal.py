# #前序遍历(中左右)
# class Solution:
#     def preorderTraversal(self, root):
#         result = []

#         def traversal(root):
#             if root == None:
#                 return
#             result.append(root.val) #中
#             traversal(root.left) #左
#             traversal(root.right) #右
        
#         traversal(root)
#         return result

# #中序遍历(左中右)
# class Solution:
#     def preorderTraversal(self, root):
#         result = []

#         def traversal(root):
#             if root == None:
#                 return
#             traversal(root.left) #左
#             result.append(root.val) #中
#             traversal(root.right) #右
        
#         traversal(root)
#         return result


# #后序遍历(左右中)
# class Solution:
#     def preorderTraversal(self, root):
#         result = []

#         def traversal(root):
#             if root == None:
#                 return
#             traversal(root.left) #左
#             traversal(root.right) #右
#             result.append(root.val) #中

#         traversal(root)
#         return result

#迭代法
#前序遍历
class Solution:
    def preorderTraversal(self, root):
        # 根结点为空则返回空列表
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            #中节点先处理
            result.append(node.value)
            #右孩子先入栈
            if node.right:
                stack.append(node.right)
            #左孩子后入栈
            if node.left:
                stack.append(node.left)
        return result


#中序遍历
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        stack = [] #不能提前将root加入stack
        result = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            if cur:     
                stack.append(cur)
                cur = cur.left		
            # 到达最左结点后处理栈顶结点    
            else:		
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右结点
                cur = cur.right	
        return result


#后序遍历
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            #中节点先处理
            result.append(node.val)
            #左孩子先入栈
            if node.left:
                stack.append(node.left)
            #右孩子后入栈
            if node.right:
                stack.append(node.right)

        #将最终的数组反转
        return result[::-1]

