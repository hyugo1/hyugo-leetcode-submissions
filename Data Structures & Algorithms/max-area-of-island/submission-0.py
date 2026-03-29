class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        queue = deque()

        def bfs(r, c):
            queue.append((r,c))
            grid[r][c] = 0
            res = 1
            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0):
                        continue

                    queue.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1


            return res


        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, bfs(r, c))


        return maxarea