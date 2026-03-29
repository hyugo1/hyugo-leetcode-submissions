class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()

        def helper(r, c):
            if (r < 0 or c < 0 or c >= COLS or r >= ROWS or board[r][c] != "O"):
                return

            board[r][c] = "T"
            helper(r + 1, c)
            helper(r, c + 1)
            helper(r - 1, c)
            helper(r, c - 1)


        for r in range(ROWS):
            if board[r][0] == "O":
                helper(r, 0)
            if board[r][COLS -1] == "O":
                helper(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                helper(0, c)
            if board[ROWS -1][c] == "O":
                helper(ROWS - 1, c)


        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O"):
                    board[r][c] = "X"
                elif (board[r][c] == "T"):
                    board[r][c] = "O"

