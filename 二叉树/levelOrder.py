from typing import Counter


class Solution:
    """二叉树层序遍历迭代解法"""
    def levelOrder(self, root):
        results = []
        if not root:
            return results
        
        from collections import deque
        que = deque([root])
        while que:
            size = len(que)
            reslut = []
            for _ in range(size):
                cur = que.popleft()
                reslut.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(reslut)
        return results


# 递归法
class Solution:
    def levelOrder(self, root):
        res = []
        def helper(root, depth):
            if not root: return []
            if len(res) == depth: res.append([]) # start the current depth
            res[depth].append(root.val) # fulfil the current depth
            if  root.left: helper(root.left, depth + 1) # process child nodes for the next depth
            if  root.right: helper(root.right, depth + 1)
        helper(root, 0)
        return res