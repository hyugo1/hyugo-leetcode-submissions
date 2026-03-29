class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        def bfs(r, c):
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                ro, co = queue.popleft()
                for dr, dc in directions:
                    nr, nc = ro + dr, co + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == '1'):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1

        return res