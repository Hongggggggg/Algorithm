# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(next = head)
        slow, fast = dummy_head, dummy_head
        while(n != 0 and fast != None):
            fast = fast.next
            n -= 1
        while(fast != None):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy_head.next