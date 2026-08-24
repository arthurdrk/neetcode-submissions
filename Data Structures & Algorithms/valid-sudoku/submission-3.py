from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1) lignes
        for i in range(9):
            row = [x for x in board[i] if x != "."]
            if len(row) != len(set(row)):
                return False

        # 2) colonnes
        for j in range(9):
            col = [board[i][j] for i in range(9) if board[i][j] != "."]
            if len(col) != len(set(col)):
                return False

        # 3) carrés 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [
                    board[x][y]
                    for x in range(i, i + 3)
                    for y in range(j, j + 3)
                    if board[x][y] != "."
                ]
                if len(square) != len(set(square)):
                    return False

        return True
