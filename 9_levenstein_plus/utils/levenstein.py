from .matrix import Matrix
from .langkit import digraphs, diacritics, ortographics
from .bidict import BiDict


class Levenstein:
    """
    Handles the creation of Matrix from given words,
    and calculates the Levenstein distance between them.
    """
    def __init__(self, word1: str, word2: str) -> None:
        self.word1 = self.__flatten_word(word1)
        self.word2 = self.__flatten_word(word2)
        self.real_words = [word1, word2]
        self.matrix = Matrix(self.word1, self.word2)
        self.array = self.matrix.array
        self.__fill()

    def __flatten_word(self, word: str) -> str:
        """ Changes digraphs to unigraphs in uppercase, i.e. 'ch' into 'H' """
        for digraph in digraphs.keys():
            word = word.replace(digraph, digraphs[digraph])

        return word

    def __check_chars(self, val: float, row: int, col: int) -> int:
        """ Checks if chars are the same or the same but with mistakes """
        # Same letters
        if self.word1[col-1] == self.word2[row-1]:
            val -= 1

        # Missing or added unnecessary diacritics
        elif diacritics.get(self.word1[col-1]) == self.word2[row-1] \
           or self.word1[col-1] == diacritics.get(self.word2[row-1]):
            val -= 0.8

        # Ortographic mistakes with digraphs: ch and rz
        elif self.word1[col-1].upper() == self.word2[row-1] \
           or self.word1[col-1] == self.word2[row-1].upper():
            val -= 0.5

        # Single-character ortographic mistakes, like u:ó
        elif ortographics.get(self.word1[col-1]) == self.word2[row-1] \
           or self.word1[col-1] == ortographics.get(self.word2[row-1]):
            val -= 0.5

        # Czeski błąd TODO

        return val

    def __calculus(self, row: int, col: int) -> float:
        """ Calculate value for given (x, y) cell """
        val1 = self.array[row][col-1] + 1
        val2 = self.array[row-1][col] + 1
        val3 = self.__check_chars(self.array[row-1][col-1] + 1, row, col)

        return min(val1, val2, val3)

    def __fill(self) -> None:
        """ Fill the matrix with computed values """
        for row_i, row in enumerate(self.array):
            for col_i, col in enumerate(row):
                if col_i > 0 and row_i > 0:
                    self.array[row_i][col_i] = self.__calculus(row_i, col_i)

    def __str__(self) -> str:
        """ Allow getting the result by simply calling the instance """
        return "{}/{}: {}".format(self.real_words[0], self.real_words[1], self.matrix.right_bottom)