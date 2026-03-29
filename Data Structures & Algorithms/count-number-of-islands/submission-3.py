class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        visited = set()
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c>= COLS or grid[r][c] == '0' or (r, c) in visited):
                return 

            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    res += 1

        return res