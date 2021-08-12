
class Solution:
    def spiralOrder(self, n):

        demi = (int)(n ** 0.5)

        dx = [1, 0 , -1, 0]

        dy = [0, 1, 0, -1]

        res = [0] * n

        x = y = 0
        
        di = 0 #方向

        for i in range(1, n + 1):

            res[4*y + x] = i

            next_x, next_y = (x + dx[di]), (y + dy[di])

            if((0 <= next_x < demi) and (0 <= next_y < demi) and (res[4 * next_y + next_x] == 0)):

                x, y = next_x, next_y

            else:
                di = (di + 1) % demi

                x, y = (x + dx[di]), (y + dy[di])

        return res

if __name__ == "__main__":
    a = Solution()
    print(a.spiralOrder(16))