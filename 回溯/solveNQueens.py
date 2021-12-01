#https://leetcode-cn.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int):
        if not n: return []
        board = [['.'] * n for _ in range(n)]
        res = []

        def isValid(board, row, col):
            #判断同一列是否冲突
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False

            # 判断左上角是否冲突
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            #判断右上角是否冲突
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtracking(board, row, n):
            if row == n:
                temp_res = []
                for temp in board:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtracking(board, row + 1, n)
                board[row][col] = '.'
        backtracking(board, 0, n)
        return res
