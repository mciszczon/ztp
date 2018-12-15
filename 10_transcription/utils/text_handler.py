import nltk
from nltk.tokenize import RegexpTokenizer


class TextHandler:
    
    def __init__(self, source: str) -> None:
        self.source = source
        self.words = RegexpTokenizer(r'\w+').tokenize(source)