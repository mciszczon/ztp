from .matrix import Matrix
from .langkit import digraphs, digraphs_reverse, diacritics, ortographics
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

        return list(word)

    def __check_chars(self, val: float, row: int, col: int) -> int:
        """ Checks if chars are the same or the same but with mistakes """
        flag = False

        # if char is uppercase, then split it into two chars and compare these chars instead of real self.word elements
        # which char? current for word1 or current for word2

        # Transposed digits
        if col < len(self.word1) and row < len(self.word2):
            ch1, ch2 = None, None
            if self.word1[col-1].isupper():
                ch1 = digraphs_reverse.get(self.word1[col-1])
            if self.word2[row-1].isupper():
                ch2 = digraphs_reverse.get(self.word2[row-1])

            if ch1 or ch2:
                # Substract 1.5 as the text for next letter will fail, giving unwanted +1
                if ch1 and not ch2:
                    if (ch1[0] == self.word2[row] and ch1[1] == self.word2[row-1]) \
                        and (ch1[1] == self.word2[row-1] and ch1[0] == self.word2[row]):
                        val -= 1.5

                if not ch1 and ch2:
                    if (self.word1[col-1] == ch2[1] and self.word1[col] == ch2[0]) \
                        and (self.word1[col] == ch2[0] and self.word1[col-1] == ch2[1]):
                        val -= 1.5

                if ch1 and ch2:
                    if (ch1[0] == ch2[1] and ch1[1] == ch2[0]) \
                        and (ch1[1] == ch2[0] and ch1[0] == ch2[1]):
                        val -= 1.5

            elif (self.word1[col-1] == self.word2[row] and self.word1[col] == self.word2[row-1]) \
                  and (self.word1[col] == self.word2[row-1] and self.word1[col-1] == self.word2[row]):
                # Swap letters
                self.word1[col-1], self.word1[col] = self.word1[col], self.word1[col-1]
                # Set flag to skip same letters check
                val -= 0.5
                flag = True

        # Same letters
        if self.word1[col-1] == self.word2[row-1] and not flag:
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