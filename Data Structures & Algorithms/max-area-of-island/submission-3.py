class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        queue = deque()
        visited = set()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(r, c):
            queue.append((r, c))
            visited.add((r, c))
            temp = 1
            while queue:
                ro, co = queue.popleft()
                for dr, dc in directions:
                    nr = ro + dr
                    nc = co + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        temp += 1
            return temp

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, bfs(r, c))
        return res