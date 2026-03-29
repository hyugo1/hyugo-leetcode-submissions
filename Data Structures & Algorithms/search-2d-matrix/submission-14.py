class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS =len(matrix)
        COLS =len(matrix[0])
        toprow = 0
        bottomrow = ROWS - 1

        while toprow <= bottomrow:
            row = (toprow + bottomrow) // 2
            if target < matrix[row][0]:
                bottomrow = row - 1
            elif target > matrix[row][-1]:
                toprow = row + 1
            else:
                break

        if not toprow <= bottomrow:
            return False

        row = (toprow + bottomrow) // 2
        l = 0
        r = COLS - 1

        while l <= r:
            col = (r + l) // 2

            if target > matrix[row][col]:
                l = col + 1
            elif target < matrix[row][col]:
                r = col - 1
            else:
                return True

        return False

