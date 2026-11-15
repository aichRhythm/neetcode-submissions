class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #so for each of the rows, we are gonna check if the next left pointer is less thn the target
        # if the right pointer is greater thanthe target, we look in the array, else we move to the next row

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