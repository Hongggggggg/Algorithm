#https://leetcode-cn.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_happy(num):
            sum = 0
            while num:
                sum += (num % 10) ** 2
                num = num // 10
            return sum

        record = set()

        while True:
            n = calculate_happy(n)
            if n == 1:
                return True
            
            if n in record:
                return False
            else:
                record.add(n)

