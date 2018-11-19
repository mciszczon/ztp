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

    def _iterate_multiplicity(self, ngrams_generator: iter) -> list():
        ngrams = list()
        while True:
            try:
                ngrams.append(next(ngrams_generator))
            except StopIteration:
                return ngrams

    def get_data(self, size: int = 1) -> Counter:
        return Counter(self._get_ngrams(size))

    def get_dataset(self, multiplicity: int = 3) -> Counter:
        ngrams = list()
        for factor in range(1, multiplicity + 1):
            ngrams_generator = self._get_ngrams(factor)
            ngrams += self._iterate_multiplicity(ngrams_generator)
        
        return Counter(ngrams)

    def __str__(self) -> str:
        return str(self.words)