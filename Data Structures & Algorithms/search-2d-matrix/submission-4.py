class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            right = len(matrix[i]) - 1
            if matrix[i][right] == target:
                return True
            elif matrix[i][right] < target:
                continue
            else:
                for j in matrix[i]:
                    if j == target:
                        return True
                    else:
                        continue
        return False