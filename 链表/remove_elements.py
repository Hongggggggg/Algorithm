# https://leetcode-cn.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next = head)
        cur_node = dummy_head
        while(cur_node.next != None):
            if(cur_node.next.val != val):
                cur_node = cur_node.next
            else:
                cur_node.next = cur_node.next.next
        return dummy_head.next
