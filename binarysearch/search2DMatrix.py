class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # clarifying questions/ assumptions: First of next row > (strictly) last prev row

        # Find potential row first
        ROWS, COLS = len(matrix), len(matrix[0])
        targetRow = 0  # dummy?

        # Use binary search to find potential row
        firstRow, lastRow = 0, ROWS - 1
        while firstRow <= lastRow:
            midRow = (firstRow + lastRow) // 2
            if target >= matrix[midRow][0] and target <= matrix[midRow][COLS - 1]:
                # potential row found
                targetRow = midRow
                break
            elif target < matrix[midRow][0]:
                lastRow = midRow - 1
            elif target > matrix[midRow][COLS - 1]:
                firstRow = midRow + 1

        # Then binary search within row
        l, h = 0, COLS - 1
        while l <= h:
            mid = l + ((h - l) // 2)
            if target == matrix[targetRow][mid]:
                return True
            elif target < matrix[targetRow][mid]:
                h = mid - 1
            elif target > matrix[targetRow][mid]:
                l = mid + 1
        return False
