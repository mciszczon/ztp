import itertools
from collections import Counter
from nltk import ngrams

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