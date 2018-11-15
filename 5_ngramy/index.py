import re
import itertools
from collections import Counter
from nltk import ngrams


class Handler:
    """
    File handler
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __words_from_line(self, line: str) -> list:
        "Zwraca listę słów dla linijki tekstu unicode."
        words = re.split(r'[\W\d]+', line)
        return [w.lower() for w in words if w]

    @property
    def lines(self) -> list:
        with open(self.filename, "r") as file:
            return file.readlines()

    @property
    def words(self) -> list:
        words = []
        for line in self.lines:
            [words.append(word) for word in self.__words_from_line(line)]
        return words

class Ngram:
    """
    Class for generating Ngrams from supplied words list
    """
    def __init__(self, words: list) -> None:
        self.words = words
        self.string = ' '.join([word for word in words])

    def _get_ngrams(self, size: int = 1) -> list:
        return ngrams(self.string, size)

    def get_data(self, size: int = 1) -> Counter:
        return Counter(self._get_ngrams(size))

    def __str__(self) -> str:
        return str(self.words)


"""
Main Block
"""

def main():
    handler = Handler("pol1.txt")
    ngram = Ngram(handler.words)

    print("Ngrams generator. Give n:")
    n = input()

    try:
        n = int(n)
        if n < 1:
            raise Exception
    except Exception:
        print("n must be an positive integer!")
        return False

    print(ngram.get_data(n))
    return True

if __name__ == "__main__":
  main()