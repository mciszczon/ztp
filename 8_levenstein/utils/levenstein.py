from .matrix import Matrix


class Levenstein:
    """
    Handles the creation of Matrix from given words,
    and calculates the Levenstein distance between them.
    """
    def __init__(self, word1: str, word2: str) -> None:
        self.word1 = word1
        self.word2 = word2
        self.matrix = Matrix(word1, word2)
        self.array = self.matrix.array
        self.__fill()

    def __calculus(self, row: int, col: int) -> int:
        """ Calculate value for given (x, y) cell """
        val1 = self.array[row][col-1] + 1
        val2 = self.array[row-1][col] + 1
        val3 = self.array[row-1][col-1] + 1

        if self.word1[col-1] == self.word2[row-1]:
            val3 -= 1

        return min(val1, val2, val3)

    def __fill(self) -> int:
        """ Fill the matrix with computed values """
        for row_i, row in enumerate(self.array):
            for col_i, col in enumerate(row):
                if col_i > 0 and row_i > 0:
                    self.array[row_i][col_i] = self.__calculus(row_i, col_i)

    def __str__(self) -> str:
        """ Allow getting the result by simply calling the instance """
        return "{}/{}: {}".format(self.word1, self.word2, self.matrix.right_bottom)