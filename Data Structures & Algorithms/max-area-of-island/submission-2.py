class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = set()
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue.append((r, c))
            visited.add((r, c))
            temp = 1
            while queue:
                ro, co = queue.popleft()
                for dr, dc in directions:
                    row = ro + dr
                    col = co + dc
                    if (0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited and grid[row][col] == 1):
                        queue.append((row, col))
                        visited.add((row, col))
                        temp += 1   
            return temp
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(bfs(r, c), res)
        
        return res