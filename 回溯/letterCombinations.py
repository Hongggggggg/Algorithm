#https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def __init__(self):
        self.answers = []
        self.answer = ''
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str):
        self.answers.clear()
        if not digits: return []
        self.backtracking(digits, 0)
        return self.answers

    def backtracking(self, digits, index):
        if index == len(digits):
            self.answers.append(self.answer)
            return 

        letters = self.letter_map[digits[index]]
        for letter in letters:
            self.answer += letter
            self.backtracking(digits, index + 1)
            self.answer = self.answer[:-1]
