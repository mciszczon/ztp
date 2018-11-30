from .matrix import Matrix


class Levenstein:

    def __init__(self, word1: str, word2: str) -> None:
        self.word1 = word1
        self.word2 = word2
        self.matrix = Matrix(word1, word2)
        self.array = self.matrix.array
        self.__calculate()

    def __calculate(self) -> int:
        for row_i, row in enumerate(self.array):
            for col_i, col in enumerate(row):
                if col_i > 0 and row_i > 0:
                    var1 = self.array[row_i][col_i-1] + 1
                    var2 = self.array[row_i-1][col_i] + 1
                    var3 = self.array[row_i-1][col_i-1] + 1

                    if self.word1[col_i-1] == self.word2[row_i-1]:
                        var3 -= 1

                    self.array[row_i][col_i] = min(var1, var2, var3)

    def __str__(self) -> str:
        return "{}/{}: {}".format(self.word1, self.word2, self.matrix.right_bottom)