class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.'] * n for i in range(n)]
        res = []
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c
        def dfs(r):
            if r== n:
                copy = ["".join(row) for row in grid]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or r + c in posDiag or r - c in negDiag:
                    continue
            
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                grid[r][c] = 'Q'
                
                dfs(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                grid[r][c] = '.'

        dfs(0)
        return res