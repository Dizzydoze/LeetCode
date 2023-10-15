class Solution:
    """Mark row and col isZero, then Set them Zero"""
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        # mark which col and row is 0
        rowflag, colflag = [False] * rows, [False] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rowflag[row] = colflag[col] = True

        for row in range(rows):
            for col in range(cols):
                if rowflag[row] or colflag[col]:
                    matrix[row][col] = 0

