class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        time, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # Start simultaneous BFS from all rotten
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    # if not unvisited fresh fruit inbound, skip
                    if (
                        newR < 0
                        or newR >= ROWS
                        or newC < 0
                        or newC >= COLS
                        or grid[newR][newC] != 1
                    ):
                        continue

                    # make rotten and add for next min
                    grid[newR][newC] = 2
                    q.append((newR, newC))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
