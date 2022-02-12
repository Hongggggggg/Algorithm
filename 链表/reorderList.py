from turtle import right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reserveList(self, head: ListNode) -> ListNode:
            pre = None
            cur = head
            while(head):
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre

    def reorderList(self, head: ListNode) -> None:
        slow, fast = head, head
        while(fast != None and fast.next != None):
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = None
        leftList = head
        rightList = self.reserveList(slow)

        n = 1
        while(leftList):
            leftTmp = leftList.next
            leftList.next = rightList
            leftList = leftTmp

            rightTmp = rightList.next
            rightList.next = leftList
            rightList = rightTmp



