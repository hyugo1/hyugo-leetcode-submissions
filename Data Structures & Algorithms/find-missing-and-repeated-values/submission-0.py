class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # for i in range(len(grid)):
        ROWS = len(grid)
        COLS = len(grid[0])
        if ROWS != COLS:
            return []
        
        seen = set()
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in seen:
                    res.append(grid[r][c])
                seen.add(grid[r][c])

        for i in range(1, ROWS * ROWS + 1):
            if i not in seen:
                res.append(i)
        return res