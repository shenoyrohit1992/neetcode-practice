class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Get dimensions
        ROWS, COLS = len(board), len(board[0])

        # 1. Discover surely unsurrounded regions at boundary
        # From the boundary Os, dfs and mark reachables as T (O -> T)

        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O":
                return

            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs(r, c)

        # 2. Whatever Os remai, can be surrounded
        # Mark them as X (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Flip the unsurrounded Os (T) back to O (T-> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
