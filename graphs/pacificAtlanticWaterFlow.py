class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()  # (r, c)
        res = []  # [r, c]

        def visitAndCheck(r, c, visit, prevHeight):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or (r, c) in visit
                or heights[r][c] < prevHeight
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                visitAndCheck(newR, newC, visit, heights[r][c])

        for c in range(COLS):
            visitAndCheck(0, c, pac, heights[0][c])
            visitAndCheck(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            visitAndCheck(r, 0, pac, heights[r][0])
            visitAndCheck(r, COLS - 1, atl, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res
