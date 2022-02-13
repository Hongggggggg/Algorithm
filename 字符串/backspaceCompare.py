#https://leetcode-cn.com/problems/backspace-string-compare/submissions/
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         n, m = len(s), len(t)
#         s_cmp, t_cmp = [], []
#         for i in range(n):
#             if s[i] != '#':
#                 s_cmp.append(s[i])
#             else:
#                 if len(s_cmp) > 0:
#                     s_cmp.pop()

#         for j in range(m):
#             if t[j] != '#':
#                 t_cmp.append(t[j])
#             else:
#                 if len(t_cmp) > 0:
#                     t_cmp.pop()

#         return True if s_cmp == t_cmp else False

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_index, t_index = len(s) - 1, len(t) - 1
        s_backspace, t_backspace = 0, 0
        while s_index >= 0 or t_index >= 0:
            while s_index >= 0:
                if s[s_index] == '#':
                    s_index -= 1
                    s_backspace += 1
                else:
                    if s_backspace > 0:
                        s_index -= 1
                        s_backspace -= 1
                    else:
                        break

            while t_index >= 0:
                if t[t_index] == '#':
                    t_index -= 1
                    t_backspace += 1
                else:
                    if t_backspace > 0:
                        t_index -= 1
                        t_backspace -= 1
                    else:
                        break

            if s_index >= 0 and t_index >= 0:
                if s[s_index] != t[t_index]:
                    return False
            elif s_index >= 0 or t_index >= 0:
                return False
            s_index -= 1
            t_index -= 1
        return True
            
