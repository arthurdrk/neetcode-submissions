class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        if not board or not board[0]:
            return
        def color(r,c):
            if min(r,c)<0 or r==ROW or c==COL or board[r][c]!="O":
                return
            board[r][c]="T"
            color(r+1,c)
            color(r,c+1)
            color(r-1,c)
            color(r,c-1)

        for r in range(ROW):
            if board[r][0]=="O":
                color(r,0)
            if board[r][COL-1]=="O":
                color(r,COL-1)
        for c in range(COL):
            if board[0][c]=="O":
                color(0,c)
            if board[ROW-1][c]=="O":
                color(ROW-1,c)
        for r in range(ROW):
            for c in range(COL):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="T":
                    board[r][c]="O"