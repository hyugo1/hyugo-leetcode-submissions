class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])  
        #search for the row where the target is

        topRow = 0
        bottomRow = ROWS - 1

        while topRow <= bottomRow:
            middleRow = topRow + ((bottomRow - topRow) // 2)

            if target > matrix[middleRow][-1]:
                topRow = middleRow + 1
            elif target < matrix[middleRow][0]:
                bottomRow = middleRow - 1

            else:
                break

        if topRow > bottomRow:
            return False
            
        row = middleRow
        l = 0
        r = COLS - 1

        while l <= r:
            m = (l+r) //2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
                
            else:
                return True


        return False



















 
        # topRow = 0
        # bottomRow = ROWS - 1

        # while topRow <= bottomRow:
        #     middleRow = (topRow + bottomRow) // 2

        #     if target > matrix[middleRow][-1]:
        #         topRow = middleRow + 1
        #     elif target < matrix[middleRow][0]:
        #         bottomRow = middleRow - 1
        #     else:
        #         break

        # if not (topRow <= bottomRow):
        #     return False

        # row = middleRow
        # l = 0
        # r = COLS - 1

        # while l <= r: 
        #     m=(l+r) // 2
        #     if target > matrix[row][m]:
        #         l = m + 1
        #     elif target < matrix[row][m]:
        #         r = m - 1
        #     else:
        #         return True

        # return False
                

            


    
