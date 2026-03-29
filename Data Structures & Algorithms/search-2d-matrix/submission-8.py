class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        topRows = 0
        bottomRows = ROWS - 1

        while topRows <= bottomRows:
            row = (topRows + bottomRows) // 2
            

            if target > matrix[row][-1]:
                topRows = row + 1

            elif target < matrix[row][0]:
                bottomRows = row - 1
            else:
                break


        if not (topRows <= bottomRows):
            return False

        row = (topRows + bottomRows) // 2 
        l = 0
        r = COLS - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True

        return False



        
            

            

