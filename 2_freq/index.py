import re
from collections import Counter


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


class Freq:
    """
    Class for calculating freq list
    """
    def __init__(self, words: list) -> None:
        self.words = words

    @property
    def freq(self) -> iter:
        """Creates frequency dict"""
        d = Counter(self.words)
        return enumerate(sorted(d.items(), key=lambda kv: kv[1], reverse=True))

    def print(self):
        """
        Prints frequency dict in form:
        position: int, word: str, num: int (number of times it appeared in the text)
        """
        for i, item in self.freq:
            print("{}, {}, {}".format(i+1, item[0], item[1]))


"""
Main Block
"""


def main():
    wiki = Handler("wiki.txt")
    freq = Freq(wiki.words)

    freq.print()

    return True


if __name__ == "__main__":
    main()
