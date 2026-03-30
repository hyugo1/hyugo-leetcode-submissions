class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows= len(matrix)
        cols= len(matrix[0])

        r_seen = set()
        c_seen = set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    r_seen.add(r)
                    c_seen.add(c)


        for r in range(rows):
            for c in range(cols):
                if r in r_seen or c in c_seen:
                    matrix[r][c] = 0

