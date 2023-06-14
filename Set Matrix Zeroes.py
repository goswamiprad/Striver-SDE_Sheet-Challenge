class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        rn = len(matrix)
        rc = len(matrix[0])
        for row in range(rn):
            for col in range(rc):
                if matrix[row][col]==0:
                    rows.add(row)
                    cols.add(col)
        
        for row in rows:
            for i in range(rc):
                matrix[row][i] = 0
        
        for col in cols:
            for i in range(rn):
                matrix[i][col] = 0
