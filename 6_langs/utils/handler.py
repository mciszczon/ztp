import re

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