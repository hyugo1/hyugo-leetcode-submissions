class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()

        directions = [[1,0], [0, 1], [0, -1], [-1, 0]]
        def bfs(r, c):
            visited.add((r,c))
            queue.append((r,c))
            temp = 1
            while queue:
                ro, co = queue.popleft()
                for dr, dc in directions:
                    nr, nc = ro + dr, co + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        temp += 1

            return temp

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(bfs(r, c), res)

        return res

            