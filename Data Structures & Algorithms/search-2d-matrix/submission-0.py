class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows*cols-1

        while low <= high:
            mid = (low+high) // 2

            row, col = mid // cols, mid % cols

            if matrix[row][col] < target: 
                low = mid + 1
            elif matrix[row][col] > target: 
                high = mid - 1
            else: 
                return True
        
        return False