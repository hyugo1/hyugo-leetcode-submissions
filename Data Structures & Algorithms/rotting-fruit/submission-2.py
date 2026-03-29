class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        fresh = 0
        visited = set()
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                ro, co = queue.popleft()
                for dr, dc in directions:
                    nr, nc = ro + dr, co + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        fresh -= 1
                        visited.add((nr, nc))
            res += 1
        
        return res if fresh == 0 else -1
