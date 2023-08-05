class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.s = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i, row in enumerate(matrix, 1):
            for j, x in enumerate(row, 1):
                self.s[i][j] = (
                    self.s[i - 1][j] + self.s[i][j - 1] - self.s[i - 1][j - 1] + x
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.s[row2 + 1][col2 + 1]
            - self.s[row2 + 1][col1]
            - self.s[row1][col2 + 1]
            + self.s[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
