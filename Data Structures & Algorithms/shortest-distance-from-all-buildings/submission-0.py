class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        # visited = set()
        distance = [[0]*COLS for _ in range(ROWS)]
        reach = [[0]*COLS for _ in range(ROWS)]
        total_houses = 0
        #total travel distance = sum_of_distance from all buildings
        #1  building
        #2  obstacle
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(r, c):
            queue.append((r,c, 0))
            visited = [[False]*COLS for _ in range(ROWS)]
            visited[r][c] = True
            steps = 0
            while queue:
                n = len(queue)
                for i in range(n):
                    r, c, dist = queue.popleft()
                    for dr, dc in directions:
                        row = r + dr
                        col = c + dc
                        if (0 <= row < ROWS and 0 <= col < COLS and not visited[row][col] and grid[row][col] == 0):
                            visited[row][col] = True
                            distance[row][col] += dist + 1
                            queue.append((row, col, dist + 1))
                            reach[row][col] += 1

        for r in range(ROWS):
            for c in range(COLS):
                # if grid[r][c] == 2:
                #     visited.add((r,c))
                if grid[r][c] == 1:
                    bfs(r, c)
                    total_houses += 1

         # Find the minimum distance
        min_dist = float('inf')
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and reach[r][c] == total_houses:
                    min_dist = min(min_dist, distance[r][c])
        
        return min_dist if min_dist != float('inf') else -1
        # return res 


