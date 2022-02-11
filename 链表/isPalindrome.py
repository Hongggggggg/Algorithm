#https://leetcode-cn.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#数组模拟
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
            cur = head
            length = 0
            while(cur):
                length += 1
                cur = cur.next

            array = [0] * length

            cur = head
            for i in range(length):
                array[i] = cur.val
                cur = cur.next

            left, right = 0, length - 1
            while(left < right):
                if(array[left] != array[right]):
                    return False
                else:
                    left += 1
                    right -= 1
            return True


#链表反转
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reserve_list(self, head):
        pre = None
        cur = head
        while(cur != None):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, pre = head, head, head
        while(fast and fast.next):
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None
        a = head
        b = self.reserve_list(slow)
        while(a):
            if(a.val == b.val):
                a = a.next
                b = b.next
            else:
                return False
        return True


        

        