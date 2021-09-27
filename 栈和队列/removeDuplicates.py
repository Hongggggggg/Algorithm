#https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for i in s:
            if res and res[-1] == i:
                res.pop()
            else:
                res.append(i)
        return "".join(res)

#双指针法：
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        slow = fast = 0
        length = len(s)
        while fast < length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]
            
            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
            
        return ''.join(res[0: slow])
