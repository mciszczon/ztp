import re
from .helpers import words_from_line

class Handler:
    """
    File handler
    """

    def __init__(self, filenames: list) -> None:
        self.filenames = filenames

    @property
    def files_contents(self) -> list:
        lines = list()
        for filename in self.filenames:
            with open(filename, "r") as file:
             lines += file.readlines()
        
        return lines
    @property
    def words(self) -> list:
        words = []
        for line in self.files_contents:
            [words.append(word) for word in words_from_line(line)]
        return words