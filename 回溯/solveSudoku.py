#https://leetcode-cn.com/problems/sudoku-solver/
class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

    
    def backtracking(self, board):
        #若有解返回True
        for i in range(len(board)):#遍历行
            for j in range(len(board[0])):#遍历列
                #若空格内有数字就跳过
                if board[i][j] != '.': continue
                for k in range(1, 10):
                    if self.is_valid(i, j, k, board):
                        board[i][j] = str(k)
                        if self.backtracking(board): return True
                        board[i][j] = '.'
                return False
        return True

    def is_valid(self, row, col, val, board):
        #判断行
        for i in range(9):
            if board[row][i] == str(val):
                return False

        #判断行
        for j in range(9):
            if board[j][col] == str(val):
                return False

        #判断同一九宫格
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(val):
                    return False
        return True
