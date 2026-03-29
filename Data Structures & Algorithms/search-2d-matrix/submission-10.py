class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        topRow = 0
        bottomRow = ROWS - 1

        while topRow <= bottomRow:
            row = (topRow + bottomRow) // 2
            
            if target > matrix[row][-1]:
                topRow = row + 1
            elif matrix[row][0] > target:
                bottomRow = row - 1
            else:
                break

        if not (topRow <= bottomRow):
            return False
        row = (topRow + bottomRow) // 2
        l = 0
        r = COLS - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif matrix[row][m] > target:
                r =  m - 1
            else:
                return True

        return False

        





        
            

            

