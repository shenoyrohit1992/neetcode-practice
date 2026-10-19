class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        numberOfIslands = 0
        visited = set()  # store: (r,c)

        def exploreBfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    newR, newC = row + dr, col + dc

                    if (
                        newR in range(ROWS)
                        and newC in range(COLS)
                        and grid[newR][newC] == "1"
                        and (newR, newC) not in visited
                    ):

                        q.append((newR, newC))
                        visited.add((newR, newC))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    exploreBfs(r, c)
                    numberOfIslands += 1
        return numberOfIslands
