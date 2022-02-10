# https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next = head)
        cur = dummy_head
        while cur.next and cur.next.next:
            tmp = cur.next.next
            cur.next.next = tmp.next
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        return dummy_head.next
            