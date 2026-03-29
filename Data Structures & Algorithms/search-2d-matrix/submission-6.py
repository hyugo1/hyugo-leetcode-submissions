class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        topRow = 0
        bottomRow = ROWS - 1

        while topRow <= bottomRow:
            midRow = (topRow + bottomRow) // 2
            if matrix[midRow][0] > target:
                bottomRow = midRow - 1
            elif matrix[midRow][-1] < target:
                topRow = midRow + 1
            else:
                break

        if not (topRow <= bottomRow):
            return False

        row = (topRow + bottomRow) //2
        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False