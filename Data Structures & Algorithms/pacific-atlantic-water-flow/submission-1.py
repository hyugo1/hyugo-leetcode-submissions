class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        ROWS = len(height)
        COLS = len(height[0])
        res = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        pac, atl = set(), set()

        def dfs(r, c, visited, prevheight):
            if (r< 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or height[r][c] < prevheight):
                return
            
            visited.add((r,c))

            dfs(r + 1, c, visited, height[r][c])
            dfs(r - 1, c, visited, height[r][c])
            dfs(r, c + 1, visited, height[r][c])
            dfs(r, c - 1, visited, height[r][c])


        for r in range(ROWS):
            dfs(r, 0, pac, height[r][0])
            dfs(r, COLS - 1, atl, height[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pac, height[0][c])
            dfs(ROWS - 1, c, atl, height[ROWS - 1][c])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))

        return res