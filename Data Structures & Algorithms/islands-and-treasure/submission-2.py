class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            ro, co = queue.popleft()
            for dr, dc in directions:
                nr, nc = ro + dr, co + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF):
                    queue.append((nr, nc))
                    grid[nr][nc] = grid[ro][co] + 1
