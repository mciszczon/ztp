import re


class Handler:
    """
    File handler
    """
    def __init__(self, filename: str, output: str) -> None:
        self.filename = filename
        self.output = output

    def __words_from_line(self, line: str) -> set:
        """ Zwraca listę słów dla linijki tekstu unicode. """
        words = re.split(r'[\s\,]+', line)
        return set([w for w in words if w])

    @property
    def lines(self) -> list:
        with open(self.filename, "r") as file:
            return file.readlines()

    @property
    def words(self) -> set:
        words = set()
        for line in self.lines:
            [words.add(word[::-1]) for word in self.__words_from_line(line)]
        return sorted(words)

    def save(self) -> None:
        """ Zapisuje do pliku słowa, każde w nowym wierszu """
        with open(self.output, "w") as file:
            for word in self.words:
                file.write(f"{word[::-1]}\n")