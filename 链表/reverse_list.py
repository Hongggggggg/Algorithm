# https://leetcode-cn.com/problems/reverse-linked-list/
#双指针
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while(cur != None):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


#递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(pre, cur):
            if not cur:
                return pre
            tmp = cur.next
            cur.next = pre
            return reverse(cur, tmp)
        return reverse(None, head)
        