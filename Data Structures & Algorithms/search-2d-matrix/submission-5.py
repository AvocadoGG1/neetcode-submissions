class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if matrix[row][0] <= target <= matrix[row][-1]:
                l = 0
                r = len(matrix[row]) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[row][0] <= target <= matrix[row][-1]:
                        if target == matrix[row][mid]:
                            return True
                        if target > matrix[row][mid]:
                            l = mid + 1
                        elif target < matrix[row][mid]: 
                            r = mid - 1 
        return False