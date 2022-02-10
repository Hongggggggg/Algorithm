#https://leetcode-cn.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#数组模拟
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