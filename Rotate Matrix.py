class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        newMat = [[0 for _ in range(n)] for i in range(n)]
        for row in range(n):
            for col in range(n):
                newMat[row][col] = matrix[n-1-col][row]
        
        for row in range(n):
            for col in range(n):
                matrix[row][col] = newMat[row][col]
