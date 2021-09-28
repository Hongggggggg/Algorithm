class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for item in tokens:
            if item not in {'+', '-', '*', '/'}:
                stack.append(item)
            else:
                first_num, second_num = stack.pop(), stack.pop()
                stack.append(str(int(eval(second_num + item + first_num))))
        return int(stack.pop())


a = Solution()

print(a.evalRPN(["4","13","5","/","+"]))
