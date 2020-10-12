# class NumMatrix:
#
#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix
#
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         return sum(sum(self.matrix[row][col1:col2+1]) for row in range(row1, row2+1)
